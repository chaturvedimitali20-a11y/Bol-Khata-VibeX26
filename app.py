from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import re

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('bolkhata.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS udhaar (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer TEXT UNIQUE,
                    amount INTEGER DEFAULT 0
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item TEXT UNIQUE,
                    qty INTEGER DEFAULT 0,
                    status TEXT
                )''')
    # Seed initial data if empty
    c.execute("SELECT COUNT(*) FROM udhaar")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO udhaar (customer, amount) VALUES ('Ramesh', 120), ('Suresh', 80)")
        c.execute("INSERT INTO inventory (item, qty, status) VALUES ('Milk (Packets)', 5, 'Low Stock - Order Needed'), ('Sugar (kg)', 12, 'In Stock')")
    conn.commit()
    conn.close()

def parse_hinglish_command(command):
    """Smart NLP parser (Adaption-ready structure) to extract Udhaar or Inventory actions."""
    cmd = command.lower()
    numbers = re.findall(r'\d+', cmd)
    amount = int(numbers[0]) if numbers else 20

    conn = sqlite3.connect('bolkhata.db')
    c = conn.cursor()

    # Check if inventory/order command
    if any(word in cmd for word in ['milk', 'doodh', 'sugar', 'cheeni', 'chai', 'patti', 'order']):
        item_name = 'Milk (Packets)' if ('milk' in cmd or 'doodh' in cmd) else ('Sugar (kg)' if ('sugar' in cmd or 'cheeni' in cmd) else 'Chai Patti (kg)')
        c.execute("SELECT qty FROM inventory WHERE item = ?", (item_name,))
        row = c.fetchone()
        if row:
            new_qty = row[0] + amount
            c.execute("UPDATE inventory SET qty = ?, status = 'Order Placed' WHERE item = ?", (new_qty, item_name))
        else:
            c.execute("INSERT INTO inventory (item, qty, status) VALUES (?, ?, 'Order Placed')", (item_name, amount))
        msg = f"Ordered {amount} units of {item_name}!"
    else:
        # Udhaar (credit) command: extract capitalized name or first word
        words = command.split()
        name = "Customer"
        ignore = {'write', 'add', 'rupees', 'rupaye', 'credit', 'udhaar', 'for', 'ke', 'ka', 'likh', 'do', 'rs'}
        for w in words:
            clean_w = re.sub(r'[^a-zA-Z]', '', w)
            if clean_w and clean_w.lower() not in ignore:
                name = clean_w.capitalize()
                break

        c.execute("SELECT amount FROM udhaar WHERE customer = ?", (name,))
        row = c.fetchone()
        if 'paid' in cmd or 'jama' in cmd or 'minus' in cmd:
            new_amt = max(0, (row[0] if row else 0) - amount)
            msg = f"Deducted ₹{amount} paid by {name}."
        else:
            new_amt = (row[0] if row else 0) + amount
            msg = f"Added ₹{amount} Udhaar for {name}."

        if row:
            c.execute("UPDATE udhaar SET amount = ? WHERE customer = ?", (new_amt, name))
        else:
            c.execute("INSERT INTO udhaar (customer, amount) VALUES (?, ?)", (name, new_amt))

    conn.commit()
    conn.close()
    return msg

@app.route('/', methods=['GET', 'POST'])
def index():
    status_msg = ""
    if request.method == 'POST':
        command = request.form.get('command', '').strip()
        if command:
            status_msg = parse_hinglish_command(command)

    conn = sqlite3.connect('bolkhata.db')
    c = conn.cursor()
    c.execute("SELECT customer, amount FROM udhaar ORDER BY amount DESC")
    udhaar_list = c.fetchall()
    c.execute("SELECT item, qty, status FROM inventory")
    inventory_list = c.fetchall()
    conn.close()

    total_udhaar = sum(row[1] for row in udhaar_list)
    return render_template('index.html', udhaar_list=udhaar_list, inventory_list=inventory_list, total_udhaar=total_udhaar, status_msg=status_msg)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

# ☕ Bol-Khata (बोल-खाता) — VibeX Codes 26 (Track 1)
**Built by:** Mitali Chaturvedi (Solo Builder)

A **10-second, hands-free voice & text *udhaar* (credit) and daily stock manager** built for Indian chaiwalas, street vendors, and small shopkeepers.

---

### 🎯 Problem Statement (Track 1)
Small street vendors and chaiwalas work 14+ hours daily serving dozens of shouting customers with wet hands. They cannot stop to unlock a phone and type in English to record customer credit (*udhaar*) or track daily stock (milk, sugar, tea leaves), leading to forgotten credit, lost income, and sudden stockouts.

### 💡 How Bol-Khata Solves It
- **One-Tap Voice & Text Input:** Vendors speak or type naturally in Hindi/English (e.g., *"Write 40 rupees credit for Mohan"* or *"Order 20 packets of milk"*).
- **Real Action Engine (Not a Chatbot):** Converts spoken commands into real `INSERT` and `UPDATE` SQL queries on a live relational database.
- **1-Click WhatsApp UPI Payment Reminders:** Generates pre-filled WhatsApp reminder links with customer names and exact pending rupee balances for effortless evening collections.

---

### 📦 Repository Contents
- `app.py` & `templates/index.html` — Complete Python + Flask + SQLite web application
- `bolkhata.db` — Pre-seeded SQLite database for instant testing
- `Bol-Khata_Mitali_Chaturvedi_ppt_PDF.pdf` — 7-Slide Final Presentation Deck
- `DemoVideo_BolKhata_MitaliChtaurvedi.mp4` — Live Working Screen-Recording Demo
- `screenshot 1.jpg` & `screenshot 2.png` — Annotated UI Screenshots

---

### 🚀 How to Run Locally
1. Ensure Python 3 and Flask are installed (`pip install flask`).
2. Run `python app.py` (or `py app.py` on Windows).
3. Open `http://127.0.0.1:5000` in Google Chrome or Microsoft Edge.

---

### 🛠️ Tech Stack & AI Disclosure
- **Tech Stack:** Python 3, Flask, SQLite3, HTML5, Tailwind CSS, Browser Web Speech API (`en-IN` / `hi-IN`), WhatsApp Deep Links (`wa.me`).
- **AI Disclosure:** Built using Python, Flask, and SQLite with AI-assisted code generation and NLP command-parsing structure (Adaption-ready).


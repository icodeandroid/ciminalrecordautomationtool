# 🕵️‍♀️ Criminal Record Automation Tool

A Django-based web scraper and records viewer that logs into [eClerksLA.com](https://www.eclerksla.com), scrapes the first 20 criminal records, stores them in a database, and displays them in a searchable, paginated frontend interface.

---

## 🚀 Features

- 🔐 Secure login to eClerksLA with email & password
- 📄 Scrapes first 20 records with name, case #, parish, charges, and more
- 🗃️ Stores records in Django models
- 🔎 Frontend with search, pagination, and detail views
- ⚙️ Admin panel to view/manage records
- 💥 Error handling with console logs
- 💻 Responsive Bootstrap-based layout

---

## 📁 Project Structure



---

## ⚙️ Setup Instructions

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/icodeandroid/ciminalrecordautomationtool.git
cd ciminalrecordautomationtool
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python manage.py migrate

python manage.py scrape_records --email="you@example.com" --password="yourpassword"
python manage.py runserver

Admin Panel
 👉 http://127.0.0.1:8000/admin/
python manage.py createsuperuser



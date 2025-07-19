# 🧳 ALX Travel App

Welcome to the **ALX Travel App** – a Django-based backend application designed to manage travel listings, bookings, and user reviews. Built with RESTful APIs using Django REST Framework, this app is structured for scalability and testability, and supports auto-generated Swagger documentation.

---

## 🚀 Features

- 🌍 Manage travel listings with availability and pricing
- 📅 Book accommodations with start/end date validation
- ⭐ Leave reviews with ratings (1–5)
- 🧪 Auto-generated test data via custom `seed` command
- 🧰 Clean API schema using DRF + Swagger (`drf_yasg`)

---

## 🏗️ Tech Stack

- **Python 3.13**
- **Django 5.2**
- **Django REST Framework**
- **SQLite3 (default)**
- **Faker** – for generating seed data
- **CORS Headers**, **drf_yasg** – for API docs and cross-origin support

---

## 🗂️ Project Structure

alx_travel_app/
├── listings/ # Listings, Bookings, and Reviews models
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── management/
│ └── commands/
│ └── seed.py # Seeds 200+ fake data entries
├── config/ # Main Django settings, urls, wsgi
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── db.sqlite3

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/cavein254/alx-travel-app.git
   cd alx-travel-app
   ```
2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **(Optional) Seed the database**
   ```bash
   python manage.py seed
   ```
5. **Start development server**
   ```bash
   python manage.py runserver
   ```

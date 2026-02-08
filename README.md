# Django URL Shortener

A simple and clean **URL Shortener application built with Django**.  
Authenticated users can shorten long URLs, track click counts, and manage their links from a dashboard.

---

## Features

- User authentication (Login / Signup / Logout)
- Create short URLs for long links
- Automatically generated short codes (Base62)
- User-specific dashboard
- Click count tracking
- Delete short URLs
- Bootstrap-based UI
---

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML, Bootstrap 5
- **Database:** SQLite
- **Auth:** Django Authentication System

---
## Installation & Setup

### 1️. Clone the Repository
git clone https://github.com/your-username/django-url-shortener.git
cd django-url-shortener

### 2️. Create & Activate Virtual Environment
python -m venv venv

Windows:
venv\Scripts\activate

Mac / Linux:
source venv/bin/activate

### 3️. Install Dependencies
pip install django

### 4️. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

### 5️. Create Superuser (Optional)
python manage.py createsuperuser

### 6️. Run the Development Server
python manage.py runserver

Open your browser and visit:
http://127.0.0.1:8000/



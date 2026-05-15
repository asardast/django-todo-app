## Django Todo App
A simple and secure Task Management application built with **Django 6.0**. This project demonstrates basic CRUD operations, database modeling, and professional security practices using environment variables.

---

## Features
**Task Management:** Create, view, and manage your daily tasks.
**Database Integration:** Uses SQLite for local development.
**Security First:** Sensitive information like `SECRET_KEY` is managed via `.env` files and kept out of version control.
**Clean Code:** Adheres to Django's best practices and project structure.

## Tech Stack
**Framework:** [Django](https://www.djangoproject.com/)
**Language:** Python 3.x
**Database:** SQLite
**Environment Management:** `python-dotenv`

---

## Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/django-todo-app.git](https://github.com/your-username/django-todo-app.git)
cd django-todo-app
https://github.com/asardast/django-todo-app/tree/main
```
### 2. Set up Virtual Environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate  # On Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configuration (.env)
Create a .env file in the root directory and add your secret key:
SECRET_KEY=your_secret_key_here
DEBUG=True

### 5. Run Migrations & Start Server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

### 6. Visit http://127.0.0.1:8000/ to see the app in action!


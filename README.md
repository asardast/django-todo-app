## Django Todo API
A secure and scalable Task Management REST API built with **Django 6.0** and **Django REST Framework (DRF)**. This project has been transitioned into a decoupled backend application, serving clean JSON data and configured with CORS to seamlessly integrate with modern frontend frameworks like **Vue.js**.

---

## Features
* **Full CRUD REST API:** Handles creating, viewing, updating, and deleting tasks via standardized HTTP methods.
* **Automated Routing:** Utilizes DRF's `DefaultRouter` for clean and automated API endpoint management.
* **CORS Enabled:** Fully configured with `django-cors-headers` to support secure cross-origin requests from frontend clients.
* **Security First:** Sensitive credentials like `SECRET_KEY` are isolated in `.env` files using `python-dotenv`.
* **Clean & Scalable Architecture:** Adheres to Django best practices, separating serialization from business logic.

## Tech Stack
* **Framework:** [Django](https://www.djangoproject.com/) & [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
* **Language:** Python 3.x
* **Database:** SQLite (with optimized relational modeling)
* **Environment Management:** `python-dotenv`
* **Cross-Origin Security:** `django-cors-headers`

---

## Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/asardast/django-todo-api.git](https://github.com/asardast/django-todo-api.git)
cd django-todo-api
```
### 2. Set up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate  # On Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configuration (.env)
Create a .env file in the root directory and add your secret key:
```bash
SECRET_KEY=your_secret_key_here
DEBUG=True
```

### 5. Run Migrations & Start Server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### 6. Visit (http://127.0.0.1:8000/api/tasks/) to see the app in action!

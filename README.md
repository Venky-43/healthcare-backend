# Healthcare Backend

This is the backend system for a Healthcare Management application, built using **Django** and **PostgreSQL**. It exposes RESTful APIs for managing healthcare data, supports user authentication, and integrates with a PostgreSQL database for reliable data storage.

---

## 🚀 Features

- Django REST Framework-based API structure
- PostgreSQL database integration
- Environment-based settings
- Scalable and modular Django app structure
- User authentication system

---

## 📂 Repository

GitHub: [Venky-43/healthcare-backend](https://github.com/Venky-43/healthcare-backend)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Venky-43/healthcare-backend.git
cd healthcare-backend

## Create a Virtual Environment

python -m venv venv
venv\Scripts\activate 

 ## Install PostgreSQL 

 Download from: https://www.postgresql.org/download/windows/

 ## 🗄️ Database Setup
 
## Step 1: Create Database & User

## Open psql terminal as the postgres user:

psql -U postgres

## CREATE DATABASE healthcare_db;
CREATE USER healthcare_user WITH PASSWORD 'your_password';

GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO healthcare_user;

\c healthcare_db

GRANT ALL ON SCHEMA public TO healthcare_user;

ALTER SCHEMA public OWNER TO healthcare_user;

## ⚙️ Django Configuration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',
        'USER': 'healthcare_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

## 🧱 Run Migrations
python manage.py runserver

python manage.py migrate

## 🚀 Start the Development Server

python manage.py runserver

## 📁 Project Structure

healthcare-backend/
├── api/                     # Your Django app (models, views, urls)
├── healthcare_backend/      # Main project folder
├── manage.py
└── requirements.txt

## 🧪 Testing

Use tools like Postman or curl to test the endpoints created in the api/ app.

## 🙋‍♂️ Author

Kothapalli Venkannababu

GitHub: https://github.com/Venky-43

## 📄 License
This project is licensed under the MIT License.

Let me know if you'd like to:
- Add `.env` support with `python-decouple` or `dotenv`
- Use Docker
- Add example API requests using Postman or cUR

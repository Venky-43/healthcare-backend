# Healthcare Backend

## Setup
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API Endpoints
- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/patients/`, `GET /api/patients/`, etc.
- `POST /api/doctors/`, `GET /api/doctors/`, etc.
- `POST /api/mappings/`, `GET /api/mappings/`, etc.

## Testing
Use Postman to test with JWT Bearer Token.

---
Let me know if you’d like a GitHub repo setup, Postman collection, or sample `.env` file too.

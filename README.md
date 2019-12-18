# django-nextmotion-task
    - https://gist.github.com/mariuccio/4f572a921e09ac11665d6148825093d2

# Create Virtual Env
    - virtualenv venv -p python3

# Activate Virtual Env - As per your OS.

# Goto Project Directory & Install Requirements.
    - pip install -r requirements.txt

# Run Server
    - python manage.py runserver

# Admin Credentials
    - URL: http://127.0.0.1:8000/admin
    - UserName: admin
    - Password: admin@123

# API URLs
    - For GET/POST
        - http://127.0.0.1:8000/api/invitations/
    
    - For PATCH/DELETE
        - http://127.0.0.1:8000/api/invitations/<str:id>/

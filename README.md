# custom_django_user_account
a django app customized for giving user login and register facility by email or mobile number or both

## Installation

Clone the repository
```bash
git clone https://github.com/iamsaviay/custom_django_account_user
```

cd into the directory
```bash
cd custom_django_account_user
```

Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

Activate the virtual environment
```bash
source venv/bin/activate
```

Install the requirements
```bash
pip install -r requirements.txt
```

Change the database parameters LIKE THIS... 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Run Migration and run the server
```
python manage.py makemigrations
python manage.py runserver
```

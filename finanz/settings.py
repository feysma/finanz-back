import os

SECRET_KEY = 'secret_key'
INSTALLED_APPS = [... , 'bcrypt',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
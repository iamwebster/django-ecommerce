from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-x$gpuegl8xhh1!nv!51#@&)04@_4rux^1h36fty32l221)@^_3"

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    ]

from .base import *

import dj_database_url
import django_heroku


ALLOWED_HOSTS = ['murmuring-ravine-49991.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'mainapp',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())

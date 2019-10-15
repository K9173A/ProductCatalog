import os

import dj_database_url
import django_heroku

from .base import BASE_DIR


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())

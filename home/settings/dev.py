'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['10.168.242.38']
DEBUG = True

WSGI_APPLICATION = 'home.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)

CORS_ORIGIN_ALLOW_ALL = True
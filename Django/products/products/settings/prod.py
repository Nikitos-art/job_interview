from .base import *

DEBUG = False

SECRET_KEY = 'django-insecure-ob48janu!(18*p&yefla@%k!rkv=(-an0p9qv-tj&m&sw1wsc4'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'products',
        'USER': 'nikita',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432',
    }
}
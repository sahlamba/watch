from settings import BASE_DIR, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "watch",
        "USER": "aman",
        "PASSWORD": "cg.9",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

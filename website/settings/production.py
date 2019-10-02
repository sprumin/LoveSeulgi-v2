from .base import *


DEBUG = False

ALLOWED_HOSTS = ["loveseulgi.kro.kr"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "db",
        "USER": "user",
        "PASSWORD": "password",
    }
}
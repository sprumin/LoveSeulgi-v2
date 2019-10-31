from .base import *

import os

# SECRET KEY
SECRET_KEY = os.urandom(40)

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
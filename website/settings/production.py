from .base import *

import os

# SECRET KEY
SECRET_KEY = os.urandom(40)

DEBUG = False

ALLOWED_HOSTS = ["loveseulgi.kro.kr"]

# S3 Storage
DEFAULT_FILE_STORAGE = "../storages.MediaStorage"
STATICFILES_STORAGE = "../storages.StaticStorage"
MEDIAFILES_LOCATION = "media"
STATICFILES_LOCATION = "static"

# AWS_ACCESS
AWS_ACCESS_KEY_ID = "AKIAROHI7HIHAKJTXION"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "loveseulgi"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(ROOT_DIR, "db.sqlite3"),
    }
}
from .base import *

import os

# SECRET KEY
SECRET_KEY = os.urandom(40)

DEBUG = False

ALLOWED_HOSTS = ["*"]

# AWS
AWS_ACCESS_KEY_ID = 'AKIAROHI7HIHKP4NFXLE'
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = 'loveseulgi-v2'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# STATIC
AWS_STATIC_LOCATION = 'static'
STATICFILES_DIRS = [
    os.path.join(ROOT_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
STATICFILES_STORAGE = 'website.storages.StaticStorage'

# MEDIA
AWS_MEDIA_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')
DEFAULT_FILE_STORAGE = 'website.storages.MediaStorage'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(ROOT_DIR, "db.sqlite3"),
    }
}
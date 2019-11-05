from .base import *

import os


# SECRET KEY
SECRET_KEY = 'u4&+la58wr7$o$ma0o$zk9z-v417fg)j!6zsdsyx^&t58z7u_('

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(ROOT_DIR, "db.sqlite3"),
    }
}

# Selenium headless browser
HEADLESS_BROWSER = "chromedriver.exe"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'

# Media files

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')
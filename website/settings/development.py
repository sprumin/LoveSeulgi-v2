from .base import *

import os


# SECRET KEY
SECRET_KEY = 'u4&+la58wr7$o$ma0o$zk9z-v417fg)j!6zsdsyx^&t58z7u_('

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
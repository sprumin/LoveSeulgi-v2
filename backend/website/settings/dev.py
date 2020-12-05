from .base import *



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q77ybs)*+4vk7ft5ns5r@2gxjx+60p&0d^l@otj$qi0n%qm-=h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
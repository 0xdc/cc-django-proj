import os

from . import env

os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("ALLOWED_HOSTS", env("C9_HOSTNAME"))

from . import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': "localhost",
        'NAME': "c9",
        'USER': env("C9_USER"),
        'PASSWORD': "",
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

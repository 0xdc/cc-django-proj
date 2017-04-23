from . import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': env("DB_DEFAULT_HOST"),
        'NAME': env("DB_DEFAULT_NAME"),
        'USER': env("DB_DEFAULT_USER"),
        'PASSWORD': env("DB_DEFAULT_PASSWORD"),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

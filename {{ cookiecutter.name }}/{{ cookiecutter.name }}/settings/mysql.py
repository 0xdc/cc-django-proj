from . import *

os.environ.setdefault("DB_DEFAULT_PORT", "3306")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': env("DB_DEFAULT_HOST"),
        'NAME': env("DB_DEFAULT_NAME"),
        'USER': env("DB_DEFAULT_USER"),
        'PORT': env("DB_DEFAULT_PORT"),
        'PASSWORD': env("DB_DEFAULT_PASSWORD"),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

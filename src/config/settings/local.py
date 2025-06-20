from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xsyb&flc!%uq7n=$#)wdx24=6hzu=l)i#+q*=zqyo@cyv_b)h-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '19901',
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
        # 'TEST': { # 테스트를 django test로 할 거면 주석 해제 후 사용
        #     'CHARSET': 'utf8',
        #     'COLLATION': 'utf8_general_ci',
        # }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# INSTALLED_APPS
DEVELOP_APPS = [
    'django_extensions',
    'apps',

]

INSTALLED_APPS = INSTALLED_APPS + DEVELOP_APPS

# SQL LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'sql': {
            '()': 'django_sqlformatter.SqlFormatter',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'sql',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}

"""
Django settings for OdonMed project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pxfi2(0n10xj$=@2ii@mxwg2_%y((_+cvxuspo&&c2c6h(!+0&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'odonmed.apps.main',
    'odonmed.apps.pacientes',
    'odonmed.apps.medicos',
    'odonmed.apps.consultas',
    'odonmed.apps.horas',
    'odonmed.apps.reservas',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'odonmed.urls'

WSGI_APPLICATION = 'odonmed.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'OdonMed',
        'USER': 'OdonMed',
        'PASSWORD': '12345',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
            'autocommit': True,
	    },
    }
}

# Internationalization


LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
DEFAULT_CHARSEt = 'utf-8'

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'odonmed/static/',),
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'odonmed/templates/'),
)
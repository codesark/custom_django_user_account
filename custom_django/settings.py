from local_settings import *
from django.utils.translation import ugettext_lazy as _

DEBUG = DEBUG
ALLOWED_HOSTS = ALLOWED_HOSTS
BASE_DIR = BASE_DIR
SECRET_KEY = SECRET_KEY

# -------------- Database Settings ------------------------
DATABASES = DATABASES


SITE_ID = 1

INSTALLED_APPS = [
    'phonenumber_field',
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'custom_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ------------- AUTH ---------------------

LOGIN_URL = '/account/signin'

AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = (
    'accounts.backends.UserAuth',
    'django.contrib.auth.backends.ModelBackend',
)


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ----------------- LOCALISATION ------------------------

LANGUAGE_CODE = 'en-in'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# --------- Static & Media Resource Management ----------

# Media Files
MEDIA_URL = MEDIA_URL
MEDIA_ROOT = MEDIA_DIR


# Static Files
STATIC_URL = STATIC_URL

if DEBUG:
    STATICFILES_DIRS = [STATIC_DIR, ]
else:
    STATIC_ROOT = STATIC_DIR


# -------------- WSGI Settings ---------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localland'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False


# -------------- WSGI Settings ---------------------------

WSGI_APPLICATION = 'custom_django.wsgi.application'


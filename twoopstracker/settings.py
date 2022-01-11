"""
Django settings for twoopstracker project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from typing import List

import sentry_sdk
from environs import Env
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

env = Env()
env.read_env()

# Core Settings
# https://docs.djangoproject.com/en/3.2/ref/settings/#core-settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Sentry
SENTRY_DSN = env.str("TWOOPSTRACKER_SENTRY_DSN", "")
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration(), CeleryIntegration()],
    send_default_pii=True,
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("TWOOPSTRACKER_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("TWOOPSTRACKER_DEBUG", False)

ALLOWED_HOSTS: List[str] = env.str("TWOOPSTRACKER_ALLOWED_HOSTS", "").split(",")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.postgres",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    # installed apps
    "corsheaders",
    "storages",
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    # Local apps
    "twoopstracker.db",
    "twoopstracker.authentication",
    "twoopstracker.authentication.providers.googlesub",
    "twoopstracker.twoops",
    "twoopstracker.twitterclient",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "twoopstracker.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "twoopstracker.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {"default": env.dj_db_url("TWOOPSTRACKER_DATABASE_URL")}

AUTH_USER_MODEL = "authentication.User"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Sites
# https://docs.djangoproject.com/en/3.2/ref/settings/#sites

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Twitter API credentials
TWOOPSTRACKER_CONSUMER_KEY = env.str("TWOOPSTRACKER_CONSUMER_KEY", "")
TWOOPSTRACKER_CONSUMER_SECRET = env.str("TWOOPSTRACKER_CONSUMER_SECRET", "")
TWOOPSTRACKER_ACCESS_TOKEN = env.str("TWOOPSTRACKER_ACCESS_TOKEN", "")
TWOOPSTRACKER_ACCESS_TOKEN_SECRET = env.str("TWOOPSTRACKER_ACCESS_TOKEN_SECRET", "")

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# Celery
CELERY_BROKER_URL = env.str("TWOOPSTRACKER_CELERY_BROKER_URL", "")
TWOOPTRACKER_STREAM_LISTENER_INTERVAL = env.int(
    "TWOOPTRACKER_STREAM_LISTENER_INTERVAL", 15
)

# Static Files
# https://docs.djangoproject.com/en/3.2/ref/settings/#static-files

# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
TWOOPSTRACKER_USE_S3 = env.bool("TWOOPSTRACKER_USE_S3", False)
if TWOOPSTRACKER_USE_S3:
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_SIGNATURE_VERSION = env.str("AWS_S3_SIGNATURE_VERSION", "s3v4")
    AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME")
    AWS_S3_FILE_OVERWRITE = env.bool("AWS_S3_FILE_OVERWRITE", False)
    AWS_LOCATION = env.str("AWS_LOCATION", "static")
    AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL", None)
    AWS_S3_VERIFY = env.bool("AWS_S3_VERIFY", True)

# REST_FRAMEWORK

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "twoopstracker.twoops.pagination.TwoopsTrackerPagination",
}

# Dj-Rest-Auth
# https://dj-rest-auth.readthedocs.io/en/2.1.11/

# Custom User Model
# https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-user-models
# TODO(kilemenis): These values are hard-coded now because we don't currently
#                  don't support sending emails. Once we do, we should move
#                  some to env vars.
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False

REST_SESSION_LOGIN = False
REST_USE_JWT = True

# TwoopsTracker
#

# OAuth2
TWOOPSTRACKER_GOOGLE_OAUTH2_CLIENT_ID = env("TWOOPSTRACKER_GOOGLE_OAUTH2_CLIENT_ID")
TWOOPSTRACKER_GOOGLE_OAUTH2_CLIENT_SECRET = env(
    "TWOOPSTRACKER_GOOGLE_OAUTH2_CLIENT_SECRET"
)

SOCIALACCOUNT_PROVIDERS = {
    "google_sub": {
        "APP": {
            "client_id": TWOOPSTRACKER_GOOGLE_OAUTH2_CLIENT_ID,
            "secret": TWOOPSTRACKER_GOOGLE_OAUTH2_CLIENT_SECRET,
            "key": "",
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
}

TWOOPSTRACKER_FRONTEND_LOGIN_URL = env(
    "TWOOPSTRACKER_FRONTEND_LOGIN_URL", "http://localhost:3000"
)
TWOOPSTRACKER_BACKEND_URL = env("TWOOPSTRACKER_BACKEND_URL", "http://localhost:8000")

TWOOPSTRACKER_SEARCH_DEFAULT_DAYS_BACK = env.int(
    "TWOOPSTRACKER_SEARCH_DEFAULT_DAYS_BACK", 7
)

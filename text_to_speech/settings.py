# import os
# from pathlib import Path
#
# from django.urls import reverse_lazy
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-uv#+6+l6zp9hb#w7i5!o&dmktd2w_m^zm$nrl0mc!lx@lxy3)4'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = [
#     "localhost",
# ]
#
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     "text_to_speech.web.apps.WebConfig",
#     "text_to_speech.accounts.apps.AccountsConfig",
#     "text_to_speech.profiles.apps.ProfilesConfig",
#     "text_to_speech.voices.apps.VoicesConfig",
#     "text_to_speech.subscriptions.apps.SubscriptionsConfig",
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'text_to_speech.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates']
#         ,
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'text_to_speech.wsgi.application'
#
#
# # Database
# # https://docs.djangoproject.com/en/5.0/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#
#
# # Password validation
# # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/5.0/topics/i18n/
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_TZ = True
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.0/howto/static-files/
#
# STATIC_URL = 'static/'
#
# STATICFILES_DIRS = (
#     BASE_DIR / 'staticfiles',
# )
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
#
# AUTH_USER_MODEL = 'accounts.TextToVoiceUser'
#
# LOGIN_REDIRECT_URL = reverse_lazy('index')
# LOGIN_URL = reverse_lazy('signin user')
#
# LOGOUT_REDIRECT_URL = reverse_lazy('base.html')
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#
# LOGGING = {
#     'version': 1,
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         }
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#         }
#     }
# }
#
# # Server name - demo-speechify-server
# # Engine - PostgreSQL - Flexible Server
# # Compute tier and size - Burstable Standard_B1ms
# # Database name - speechify_db
# # Region - Germany West Central
# # Username - zdspvvjgmx
# # Password - rEYDKcYr2Ss$VdY$
#
# STRIPE_PUBLIC_KEY = 'pk_test_51P2gLFIW3JPFeSCL2euoqRmgOL4EqIqrIYukcK3fjLjbiD92YosLDx3pYtIh0t02vWYFgpDR7Un61QCUs1CN1AyL00VhrDNdk2'
# STRIPE_SECRET_KEY = 'sk_test_51P2gLFIW3JPFeSCLJ7RgY1swzPJQFF8jWk8eB1UQRFJTG9ogsFLcGO8ekaxTeF5R0OMKPkp76JoEKUUmPfPm0STG001dQ8mn1T'


import os
from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uv#+6+l6zp9hb#w7i5!o&dmktd2w_m^zm$nrl0mc!lx@lxy3)4'


DEBUG = os.environ.get("DEBUG", 1)

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(" ")
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "text_to_speech.web.apps.WebConfig",
    "text_to_speech.accounts.apps.AccountsConfig",
    "text_to_speech.profiles.apps.ProfilesConfig",
    "text_to_speech.voices.apps.VoicesConfig",
    "text_to_speech.subscriptions.apps.SubscriptionsConfig",
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

ROOT_URLCONF = 'text_to_speech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'text_to_speech.wsgi.application'

# ENABLE_ORYX_BUILD = True
# Database

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRES_HOST'),
            'PORT': os.environ.get('POSTGRES_PORT'),
        }
    }

# Password validation


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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)

STATIC_ROOT = BASE_DIR / 'static'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.TextToVoiceUser'

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('signin user')

LOGOUT_REDIRECT_URL = reverse_lazy('base.html')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

# Server name - demo-speechify-server
# Engine - PostgreSQL - Flexible Server
# Compute tier and size - Burstable Standard_B1ms
# Database name - speechify_db
# Region - Germany West Central
# Username - zdspvvjgmx
# Password - rEYDKcYr2Ss$VdY$

STRIPE_PUBLIC_KEY = 'pk_test_51P2gLFIW3JPFeSCL2euoqRmgOL4EqIqrIYukcK3fjLjbiD92YosLDx3pYtIh0t02vWYFgpDR7Un61QCUs1CN1AyL00VhrDNdk2'
STRIPE_SECRET_KEY = 'sk_test_51P2gLFIW3JPFeSCLJ7RgY1swzPJQFF8jWk8eB1UQRFJTG9ogsFLcGO8ekaxTeF5R0OMKPkp76JoEKUUmPfPm0STG001dQ8mn1T'

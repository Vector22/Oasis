"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
# For ABSOLUTE_URL_OVERRIDES
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5^w!dbg4(@cnun_u)w7#tb&gv7-z!lozpa)pkxj%+=q_g)z*0@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['oasis.com', 'localhost', '127.0.0.1',
                 '5d325d16.ngrok.io']


# Application definition

INSTALLED_APPS = [
    # thirds party apps
    'social_django',
    'sorl.thumbnail',
    # locals apps
    'account.apps.AccountConfig',
    'images.apps.ImagesConfig',
    'actions.apps.ActionsConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Dummy cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '../media/images_uploaded_cache',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 100
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Serving Media files like user's photos and others

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Login and logout settings

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Allowing social authentication by facebook, and gmail

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # Facebook social-auth
    'social_core.backends.facebook.FacebookOAuth2',
    # Google social-auth
    'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_FACEBOOK_KEY = '403005740348518'  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '82c139ef2e1a71a463645bb966759b4a'  # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '373723408738-uh0l60pb8a33ssbmj6ce9tdulb34dmtm.apps.googleusercontent.com'
# Google Consumer Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'iBJky8RwwzUog80yujsJr0aZ'


# Another way to define a get_absolute_url
# to specify an URL for a model

ABSOLUTE_URL_OVERRIDES = {
    # Add dynamically a get_absolute_url method to auth.user model
    'auth.user': lambda u: reverse_lazy('user_detail',
                                        args=[u.username])
}

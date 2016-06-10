"""
Django settings for aqhorajuega project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v-k-u-h4+0$i50pw51n4+l84mh(l)&zvw0uuh3!$w%rfqv=063'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS = ['aquehorajuegaargentina.com', '54.93.126.245:8001']


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'timezone_field',
    'main',
    'cities_light',
    'cities',
    'aqhj_sites',
    'storages',
    'redactor',
    'compressor',
]

CITIES_LIGHT_APP_NAME = 'cities'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aqhorajuega.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processor.get_current_path',
                'main.context_processor.main_season_cp',
                'main.context_processor.time_format_cp',
                'main.context_processor.domain_team_cp',
                'main.context_processor.settings_cp',
                'aqhj_sites.context_processor.sites_config_cp',
                'django.core.context_processors.static'
                "django.core.context_processors.i18n",
                'aqhj_sites.context_processor.sites_config_cp',
            ],
        },
    },
]

WSGI_APPLICATION = 'aqhorajuega.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#sng!5n6;)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aqhj_dev',  # TEAM_TYPE_DOMAIN VARIABLE
        'USER': 'aqhj_user',
        'PASSWORD': 'aqhj12348765',
        'HOST': 'sng.ces9zlqxeeow.eu-central-1.rds.amazonaws.com',
        'OPTIONS': {
                    'charset': 'utf8',
                    'use_unicode': True, },
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

GEOIP_PATH = 'geoip'

GOOGLE_API_KEY = "AIzaSyA0_HDVu33cDbT-dEjaEcin0FIdWO0SNXc"
GOOGLE_TZ_API_ENDPOINT = 'https://maps.googleapis.com/maps/api/timezone/json'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
AWS_STORAGE_BUCKET_NAME = 'aqhj-files-dev'  # TEAM_TYPE_DOMAIN VARIABLE
AWS_ACCESS_KEY_ID = os.environ('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ('AWS_SECRET_ACCESS_KEY')

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#STATIC_URL = '/static/'
MEDIA_FILES_LOCATION = "aqhj/media"
STATIC_FILES_LOCATION = "aqhj/static"
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATIC_FILES_LOCATION)
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIA_FILES_LOCATION)
STATICFILES_STORAGE = 'aqhorajuega.s3utils.StaticRouteS3BotoStorage'
DEFAULT_FILE_STORAGE = 'aqhorajuega.s3utils.MediaRouteS3BotoStorage'

REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_FILE_STORAGE = 'aqhorajuega.s3utils.MediaRouteS3BotoStorage'

COMPRESS_STORAGE = STATICFILES_STORAGE
COMPRESS_ENABLED = True
COMPRESS_ROOT = 'compress'
COMPRESS_OFFLINE = True
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',  'compressor.filters.cssmin.CSSMinFilter']
AQHJ_DOMAIN = 'http://54.93.126.245:8001'
LOCALE_PATHS = (BASE_DIR + "/locale/",)
BET_AFFILIATE_LINK = 'http://www.bet365.com/dl/~offer?affiliate=365_482502'
SITE_ID = 1

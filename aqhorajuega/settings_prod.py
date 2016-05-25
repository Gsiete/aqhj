from . import settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = settings.BASE_DIR
# Application definition
INSTALLED_APPS = settings.INSTALLED_APPS
CITIES_LIGHT_APP_NAME = settings.CITIES_LIGHT_APP_NAME
MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES
ROOT_URLCONF = settings.ROOT_URLCONF
TEMPLATES = settings.TEMPLATES
WSGI_APPLICATION = settings.WSGI_APPLICATION
# Password validation
AUTH_PASSWORD_VALIDATORS = settings.AUTH_PASSWORD_VALIDATORS
# Internationalization
LANGUAGE_CODE = settings.LANGUAGE_CODE
TIME_ZONE = settings.TIME_ZONE
USE_I18N = settings.USE_I18N
USE_L10N = settings.USE_L10N
USE_TZ = settings.USE_TZ
# Custom
GEOIP_PATH = settings.GEOIP_PATH
GOOGLE_API_KEY = settings.GOOGLE_API_KEY
GOOGLE_TZ_API_ENDPOINT = settings.GOOGLE_TZ_API_ENDPOINT
# Static files (CSS, JavaScript, Images)
# AWS
AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
AWS_HEADERS = settings.AWS_HEADERS
MEDIA_FILES_LOCATION = settings.MEDIA_FILES_LOCATION
STATIC_FILES_LOCATION = settings.STATIC_FILES_LOCATION
STATICFILES_STORAGE = settings.STATICFILES_STORAGE
DEFAULT_FILE_STORAGE = settings.DEFAULT_FILE_STORAGE
COMPRESS_STORAGE = settings.COMPRESS_STORAGE
# Django-Compressor
COMPRESS_ROOT = settings.COMPRESS_ROOT
COMPRESS_OFFLINE = settings.COMPRESS_OFFLINE
COMPRESS_CSS_FILTERS = settings.COMPRESS_CSS_FILTERS
STATICFILES_FINDERS = settings.STATICFILES_FINDERS
# REDACTOR_OPTIONS
REDACTOR_OPTIONS = settings.REDACTOR_OPTIONS
REDACTOR_FILE_STORAGE = settings.REDACTOR_FILE_STORAGE
# AWS URLs
AWS_STORAGE_BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATIC_FILES_LOCATION)
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIA_FILES_LOCATION)

# Database
DATABASES = settings.DATABASES
DATABASES['default']['NAME'] = 'aqhj'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vsk-u:h4+0$i50pw51n4+l84mh(l)&spijpa3!$w%rfqv=06'
DEBUG = False
ALLOWED_HOSTS = ['aquehorajuegaargentina.com']
COMPRESS_ENABLED = False
AQHJ_DOMAIN = 'http://aquehorajuegaargentina.com'
COMPRESS_REBUILD_TIMEOUT = settings.COMPRESS_REBUILD_TIMEOUT
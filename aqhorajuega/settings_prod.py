from .settings import *

# AWS URLs
AWS_STORAGE_BUCKET_NAME = 'sng-files2'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATIC_FILES_LOCATION)
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIA_FILES_LOCATION)

# Database
DATABASES['default']['NAME'] = 'aqhj'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vsk-u:h4+0$i50pw51n4+l84mh(l)&spijpa3!$w%rfqv=06'
DEBUG = False
ALLOWED_HOSTS = ['aquehorajuegaargentina.com']
COMPRESS_ENABLED = True
AQHJ_DOMAIN = 'http://aquehorajuegaargentina.com'
SITE_ID = 1
LANGUAGE_CODE = 'es-ar'

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

StaticRouteS3BotoStorage = lambda: S3BotoStorage(location=settings.STATIC_FILES_LOCATION)
MediaRouteS3BotoStorage = lambda: S3BotoStorage(location=settings.MEDIA_FILES_LOCATION)

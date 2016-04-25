from storages.backends.s3boto import S3BotoStorage

StaticRouteS3BotoStorage = lambda: S3BotoStorage(location='aqhj/static')
MediaRouteS3BotoStorage = lambda: S3BotoStorage(location='aqhj/media')

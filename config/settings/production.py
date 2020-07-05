import os
from .base import *

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
ALLOWED_HOSTS = os.environ["DJANGO_ALLOWED_HOSTS"].split(" ")

DEBUG = False

INSTALLED_APPS += [
    'storages',
]

AWS_ACCESS_KEY_ID = os.environ['S3_ACCESS_ID']
AWS_SECRET_ACCESS_KEY = os.environ['S3_ACCESS_SECRET']

AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
AWS_S3_ENDPOINT_URL = os.environ['S3_ENDPOINT']
AWS_S3_CUSTOM_DOMAIN = os.environ['S3_CUSTOM_DOMAIN']

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_LOCATION)
STATIC_ROOT = 'staticfiles/'

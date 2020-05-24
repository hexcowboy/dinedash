import os

from .base import *

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

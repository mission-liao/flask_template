from datetime import timedelta
from utils import get_root_path
import os

# TODO: patch it in product
SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'

REMEMBER_COOKIE_DURATION = timedelta(days=7)

# debug
DEBUG = True 
PROPAGATE_EXCEPTION = True
PRESERVE_CONTEXT_ON_EXCEPTION = True

# celery
CELERY_BROKER_URL = 'amqp://'

# sqlalchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(get_root_path(), 'test.db')

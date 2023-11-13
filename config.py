import os
from os import environ

class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'mangesh@123'

    UPLOADS = "/home/username/app/app/static/uploads"

    SESSION_COOKIES_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIES_SECURE = False

class DebugConfig(Config):
    DEBUG = False
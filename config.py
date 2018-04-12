import os

class Configuration(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this_is_the_secret_key'
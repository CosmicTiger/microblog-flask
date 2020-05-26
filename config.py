import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sh0w1ng-y0ur-tru3-f0rm'
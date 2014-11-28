import os

settings = __import__(os.environ.get('SETTINGS_MODULE'), fromlist=['*'])

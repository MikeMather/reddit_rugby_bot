import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    API_KEY = os.environ["API_KEY"]
    USERNAME = os.environ["REDDIT_USERNAME"]
    PASSWORD = os.environ["REDDIT_PASSWORD"]
    CLIENT_ID = os.environ["CLIENT_ID"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    DATABASE_URL = os.environ["DATABASE_URL"]

class ProductionConfig(Config):
    DEBUG = False
    SUBREDDIT = "rugbyunion"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SUBREDDIT = "testingground4bots"

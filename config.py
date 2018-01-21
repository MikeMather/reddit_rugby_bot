import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    API_KEY = os.environ["API_KEY"]
    REDDIT_USERNAME = os.environ["REDDIT_USERNAME"]
    REDDIT_PASSWORD = os.environ["REDDIT_PASSWORD"]

class ProductionConfig(Config):
    DEBUG = False
    SUBREDDIT = "rugbyunion"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SUBREDDIT = "testingground4bots"

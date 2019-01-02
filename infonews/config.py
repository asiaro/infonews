import logging
from datetime import timedelta
from redis import Redis

class config(object):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="sqlite:///infonews"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    REDIS_HOST="127.0.0.1"
    REDIS_PORT=6379
    SESSION_TYPE="redis"
    SESSION_USE_SIGNER=True
    SECRET_KEY="key"
    PERMANENT_SESSION_LIFETIME= timedelta(day=7)
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True

class  DevelopmentConfig(config):
    DEBUG=True
    LOG_LEVEL=logging.DEBUG


class ProductionConfig(Config):    
    DEBUG=False
    LOG_LEVEL=logging.ERROR

config_dict={
    "dev":DevelopmentConfig,
    "pro":ProductionConfig
}
        









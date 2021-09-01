import os
import logging
from logging.handlers import TimedRotatingFileHandler

BUCKET_NAME = "elytics-dev-data"
GCP_SERVICE_ACCOUNT_KEY_PATH = "gcpKey/elytics-321404-d1d205eed5e6.json"
GCP_BUCKET_PATH = "https://storage.cloud.google.com/elytics-dev-data/brand-logo"

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s  %(name)s %(threadName)s :- %(message)s")

#handler = TimedRotatingFileHandler(
#    'log/elytics-server.log', when="midnight", interval=1, encoding='utf8')
#handler.suffix = "%Y-%m-%d_%H-%M-%S"
#handler.setFormatter(formatter)
#logger = logging.getLogger()
#logger.setLevel(logging.INFO)
#logger.addHandler(handler)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    DATABASE_USER = 'elAdmin'
    DATABASE_NAME = 'el_dev'
    DATABASE_PASSWORD = 'email123'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 27017
    MONGODB_CONNECT = False
    
    MONGODB_SETTINGS = {
        'host': f'mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}?authSource={DATABASE_NAME}',
        'connect': False,
    }
    

class TestingConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    DATABASE_USER = 'elAdmin'
    DATABASE_NAME = 'el_dev'
    DATABASE_PASSWORD = 'email123'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 27017
    MONGODB_CONNECT = False

    MONGODB_SETTINGS = {
        "host": f"mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}?authSource={DATABASE_NAME}"
    }


class ProductionConfig(Config):
    """
    Production Environment Config FIle Configuration
    Environment Required Variable:
        variable         :     operation                 :      example
    ==================================================================================================================
        DATABASE_USER    : export user name              :       "root"
        DATABASE_NAME    : export name                   :       "mydb"
        DATABASE_PASSWORD: export DATABASE_USER password :       "xyz"
        DATABASE_URI     : export databse URI            :       IP Address
        DATABASE_PORT    : export port                   :       "5432"
    ==================================================================================================================
    """
    TESTING = False
    DEBUG = False
    ENV = 'production'

    DATABASE_USER = 'elAdmin'
    DATABASE_NAME = 'el_dev'
    DATABASE_PASSWORD = 'email123'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 27017
    MONGODB_CONNECT = False
    MONGODB_SETTINGS = {
        'host': f'mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}?authSource={DATABASE_NAME}',
        'connect': False,
    }


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

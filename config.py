#!/usr/bin/env python

import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
# host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']


class Config(object):   
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5438"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'test.db')

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI', default="sqlite:///" + os.path.join(basedir, 'prod.db'))

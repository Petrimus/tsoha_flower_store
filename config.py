#!/usr/bin/env python

import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
production_database_url = os.getenv('DATABASE_URL')
development_database_url = os.getenv('POSTGRES_URL')
database = os.environ['DATABASE_URL']


class Config(object):   
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = development_database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'test.db')

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = database
    
    

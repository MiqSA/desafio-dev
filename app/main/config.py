import os
import json
from sqlalchemy import create_engine
import mysql.connector
from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(__file__))

# Get credentials
_USERDB = os.getenv('USER')
_PASSWORD = os.getenv('PASSWORD')
_HOST = os.getenv('HOST')
_PORT = os.getenv('PORT')
_DATABASE = os.getenv('DATABASE')


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql://{_USERDB}:{_PASSWORD}@{_HOST}:{_PORT}/{_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI ='test.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

class ConnectionDB():
    def __init__(self):
        self.URI = f'mysql://{_USERDB}:{_PASSWORD}@{_HOST}:{_PORT}/{_DATABASE}'

    def get_engine(self):
        try:
            engine = create_engine(self.URI)
            return engine
        except Exception as err:
            print('Error in dbconfig: ', err)
            return {'msg': 'Bad Request. Erro in conection!'}, 400


class Database():
    def __init__(self):
        pass

    def create_database(self):
        try:
            mydb = mysql.connector.connect(
                host=_HOST,
                user=_USERDB,
                password=_PASSWORD
            )
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE store_manager!")
            print('Success in create database')
        except Exception as err:
            print('Error in create database!', err)


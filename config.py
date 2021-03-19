from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
    
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    # DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/democrudb'
    # DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
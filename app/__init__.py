from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app_config

db = SQLAlchemy()

# def create_app(config_name):
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_object(app_config[config_name])
#     app.config.from_pyfile('config.py')
#     db.init_app(app)

#     # temporary route
#     @app.route('/')
#     def hello_world():
#         return 'Hello, World!'

#     return app

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    app.config.from_object('myconfig.DevConfig')
    db.init_app(app)

    # temporary route
    @app.route('/')
    def hello_world():
        return 'the environments configuration are working :B!'

    return app
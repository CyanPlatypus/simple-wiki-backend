import os

from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth

from view import articles, users

config = {
  'ORIGINS': [
    'http://localhost:4200',  
    'http://127.0.0.1:4200',  
  ]  }

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    #CORS(app, support_credentials=True)
    CORS(app, resources={ r'/*': {'origins': config['ORIGINS']}}, supports_credentials=True)

    app.register_blueprint(articles.bp)
    app.register_blueprint(users.bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

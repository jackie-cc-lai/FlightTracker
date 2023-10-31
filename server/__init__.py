import os
from server.config.redis_config import redis_config
from flask_caching import Cache
from flask import Flask
from flask_cors import CORS
from server.routes.get import getViews
from server.routes.auth import authViews
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_mapping(redis_config)

    host = os.environ['DB_URL']
    database = os.environ['DB_NAME']
    user = os.environ['DB_USERNAME']
    password = os.environ['DB_PASSWORD']
    port = os.environ['DB_PORT']

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{pw}@{url}:{port}/{db}'.format(
        user=user, pw=password, url=host, db=database, port=int(port))

    # silence the deprecation warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    cache = Cache(app)  # Initialize Cache
    CORS(app, origins=os.environ['FLASK_ALLOWED_ORIGINs'])

    getViews(app)
    authViews(app)

    return app

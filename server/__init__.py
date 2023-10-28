import os
from server.config.redis_config import redis_config
from flask_caching import Cache
from flask import Flask
from flask_cors import CORS
from server.routes.get import getViews

def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_mapping(redis_config)
    cache = Cache(app)  # Initialize Cache
    CORS(app, origins=os.environ['FLASK_ALLOWED_ORIGINs'])

    getViews(app)
    
    return app
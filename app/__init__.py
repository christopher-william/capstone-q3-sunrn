from environs import Env
from flask import Flask
from flask_jwt_extended import JWTManager

from .models import configure as models_configure
from .schema import configure as schemas_configure
from .views import configure as views_configure

configs = {
    'development': 'DevelopmentConfig',
    'production': 'ProductionConfig',
    'test': 'TestingConfig'
}


def create_app(config='test'):
    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config.from_object(f'config.{configs[config]}')

    models_configure(app)
    schemas_configure(app)
    views_configure(app)
    JWTManager(app)

    return app

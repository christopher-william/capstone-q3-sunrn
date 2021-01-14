from environs import Env
from flask import Flask

from .models import configure as db_configure
from .models import db, mg
from .views import configure as views_configure


def create_app(mode='development'):
    env = Env()
    env.read_env()

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool(
        'SQLALCHEMY_TRACK_MODIFICATIONS'
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')

    db_configure(app)
    views_configure(app)

    return app

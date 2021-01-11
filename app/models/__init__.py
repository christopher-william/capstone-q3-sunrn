from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
# from marshmallow import fields

db = SQLAlchemy()
mg = Migrate()
# ma = Marshmallow()


class Populate_hsp(db.Model):
    id = db.

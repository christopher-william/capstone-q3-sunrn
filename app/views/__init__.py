from flask import Flask
from flask_restful import Api

from .seller import SellerRoute


def configure(app: Flask):

    api = Api(app)
    api.add_resource(SellerRoute, '/seller')

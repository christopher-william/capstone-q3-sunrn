from flask import Flask
from flask_restful import Api

from .seller import SellerLogin, SellerRegister


def configure(app: Flask):

    api = Api(app)
    api.add_resource(SellerRegister, '/seller')
    api.add_resource(SellerLogin, '/login')

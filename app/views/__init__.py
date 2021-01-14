from flask import Flask
from flask_restful import Api

from .seller_view import SellerLogin, SellerRegister
from .hsp_view import HspsByUf, HspUf


def configure(app: Flask):

    api = Api(app)
    api.add_resource(SellerRegister, '/register')
    api.add_resource(SellerLogin, '/login')
    api.add_resource(HspUf, '/hsp')
    api.add_resource(HspsByUf, '/hsp/<string:uf>')

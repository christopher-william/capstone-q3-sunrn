from flask import Flask
from flask_restful import Api

from .seller_view import SellerLogin, SellerRegister
from .message_view import Message


def configure(app: Flask):

    api = Api(app)
    api.add_resource(SellerRegister, '/register')
    api.add_resource(SellerLogin, '/login')

    api.add_resource(Message, '/message/<int:id>')
    api.add_resource(Message, '/message')

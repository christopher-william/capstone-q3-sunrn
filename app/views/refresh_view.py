from flask_jwt_extended import (
    jwt_refresh_token_required, 
    get_jwt_identity,
    create_access_token
    )
from flask import request
from flask_restful import Resource
from datetime import timedelta

class Refresh(Resource):
    @jwt_refresh_token_required
    def get(self):
        user_id = get_jwt_identity()
        acess_token = create_access_token(
            identity=user_id,
            expires_delta=timedelta(days=1)
        )

        return {'acess_token':acess_token}


from http import HTTPStatus

from app.models.hsp_model import Hsp, hsps_schema
from sqlalchemy.exc import IntegrityError

from .http import build_api_response


def get_uf_or_all(**kwargs):
    try:
        uf = kwargs["uf"]
        
        
        print("yo")
    
    except:
        ufs = Hsp.query.filter_by(uf="ACRE").all()

        ufschema = hsps_schema.dump(ufs)
        print(ufschema)

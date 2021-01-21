from http import HTTPStatus

from ..models import Hsp
from ..schema import hsps_schema

from .http_service import build_api_response


def get_uf_or_all(**kwargs):
    try:
        uf = kwargs["uf"].upper()
        ufs = Hsp.query.filter_by(uf=uf).all()
        if not len(ufs):
            return build_api_response(HTTPStatus.BAD_REQUEST)

        return build_api_response(HTTPStatus.OK, {
            "data": hsps_schema.dump(ufs)})

    except Exception as error:
        print(error)
        
        uf_query = Hsp.query.order_by(Hsp.uf).all()
        uf_schema = hsps_schema.dump(uf_query)
        uf_list = [uf.get("uf") for uf in uf_schema]
        uf_filtred = list(set(uf_list))

        return build_api_response(HTTPStatus.OK, {"uf": uf_filtred})

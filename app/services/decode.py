import jwt


def encode_password(data):
    criptography = jwt.encode({'email': data['email'], data['password'], algorithm="HS256"})
    return criptography

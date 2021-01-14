import jwt


def encode_password(data):
    try:
        criptography = jwt.encode(
            {'email': data['email']}, data['password'], algorithm="HS256")

    except:
        return None

    return str(criptography)

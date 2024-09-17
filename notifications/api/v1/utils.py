import datetime
import jwt
from django.conf import settings


def generate_access_token(user):
    access_token_payload = {
        "user_id": str(user.id),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30),
        #"exp": datetime.datetime.utcnow() + datetime.timedelta( minutes=1),
        "iat": datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(
        access_token_payload, settings.SECRET_KEY, algorithm="HS256"
    )
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        "user_id": str(user.id),
        #"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30),
        "iat": datetime.datetime.utcnow(),
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.SECRET_KEY, algorithm="HS256"
    )
    return refresh_token

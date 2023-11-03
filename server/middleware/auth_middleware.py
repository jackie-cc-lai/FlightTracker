from functools import wraps
import jwt
import os
from flask import request, abort
from flask import current_app
from server.service.user import get_user


def token_required(f):
    @wraps(f)
    def verify(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token or token == 'null':
            print('no token')
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            data = jwt.decode(
                token, os.environ['JWT_SECRET_KEY'], algorithms=["HS256"])
            current_user = get_user(data)
            if current_user is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return verify


def generate_jwt(user):
    jwt_secret = os.environ['JWT_SECRET_KEY']
    return jwt.encode(user, jwt_secret, algorithm="HS256")

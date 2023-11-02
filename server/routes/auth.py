from server.service.auth import get_user, generate_jwt
from flask import request, Response
import json
from hashlib import sha256


def authViews(app):
    @app.route('/login', methods=['POST'])
    def auth():
        data = request.get_json()
        userData = get_user(data)
        if userData is None:
            print('no user found')
            return Response(
                "No user found",
                status=400
            )
        else:
            password = sha256(data['password'].encode(
                encoding='UTF-8', errors='strict')).hexdigest()
            if userData['password'] == password:
                user = dict((field, userData[field]) for field in (
                    'id', 'email', 'name', 'created_on'))
                token = generate_jwt(user)

                response = json.dumps(dict(token=token, user=user))
                return Response(
                    response=response,
                    status=200
                )
            else:
                return Response(
                    "Login failed",
                    status=401
                )

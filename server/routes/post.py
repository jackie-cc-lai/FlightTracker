import json


from server.middleware.auth_middleware import token_required
from server.service.flight_service import save
from flask import request, Response
from schema import Schema, And, Use, Optional, SchemaError


def postViews(app):
    @app.route('/save-flight', methods=['POST'])
    @token_required
    def save_flight(current_user):
        data = request.get_json()
        try:
            save(current_user['id'], data['flight'])
            return Response(
                response='Flight saved',
                status=201
            )
        except:
            return Response(
                response='Cannot save flight',
                status=500
            )

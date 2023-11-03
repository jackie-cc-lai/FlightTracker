from server.middleware.auth_middleware import token_required
from server.service.flight_service import save_flight
from flask import request, Response
from schema import Schema, And, Use, Optional, SchemaError


def postViews(app):
    @token_required
    @app.route('/save', method=['POST'])
    def save_flight(current_user):
        data = request.get_json()
        try:
            save_flight(current_user['id'], data)
            return Response(
                response='Flight saved',
                status=201
            )
        except:
            return Response(
                response='Cannot save flight',
                status=500
            )

from flask import request, Response
import json
import os

from server.middleware.auth_middleware import token_required
from server.service.flight_api import search_by_ident_iata
from server.service.flight_service import get_user_flights


def getViews(app):
    @app.route('/search-flights')
    @token_required
    def search_flights(current_user):
        flight_id = str(request.args.get('flightId'))
        print(flight_id)
        flight_data = search_by_ident_iata(flight_id)
        return flight_data

    @app.route('/user-flights')
    @token_required
    def get_flights(current_user):
        flights = get_user_flights(current_user['id'])
        response = json.dumps([flight['flight_data']
                               for flight in flights])
        return Response(
            response=response,
            status=200
        )

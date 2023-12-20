from flask import request, Response
import json
import os

from server.middleware.auth_middleware import token_required
from server.service.db import get_flights_by_ids
from server.service.flight_api import search_by_ident_iata
from server.service.flight_service import get_user_flights


def getViews(app, cache):
    @app.route('/search-flights')
    @token_required
    @cache.cached(timeout=120, query_string=True)
    def search_flights(current_user):
        flight_id = str(request.args.get('flightId'))
        flight_data = search_by_ident_iata(flight_id)
        return flight_data

    @app.route('/flights')
    @token_required
    @cache.cached(timeout=60, query_string=True)
    def get_flights(current_user):
        flights = get_user_flights(current_user['id'])
        response = json.dumps([flight['flight_data']
                               for flight in flights])
        return Response(
            response=response,
            status=200
        )

    @app.route('/flight')
    @token_required
    def get_flight(current_user):
        flight_id = str(request.args.get('flightId'))
        flight = get_flights_by_ids([flight_id])
        response = json.dumps(flight[0]['flight_data'])
        return Response(
            response=response,
            status=200
        )

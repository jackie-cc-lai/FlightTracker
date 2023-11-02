from flask import request
import json
import os

from server.middleware.auth_middleware import token_required
from server.service.flight_api import search_flights


def getViews(app):
    @app.route('/searchFlights')
    @token_required
    def searchFlights(current_user):
        flight_id = str(request.args.get('flightId'))
        # flight_data = search_flights(flight_id)
        fileDirectory = os.getcwd()
        jsonPath = os.path.join(fileDirectory, 'server',
                                'mock', 'mockSearch.json')
        with open(jsonPath, 'r') as flightDataFile:
            flight_data = json.load(flightDataFile)
        return flight_data

    @app.route('/getFlights')
    def getFlights(current_user):
        # call db to get stuff
        return 'list of flights'

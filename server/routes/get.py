from flask import request
import json
import os

from server.middleware.auth_middleware import token_required


def getViews(app):
    @app.route('/searchFlights')
    @token_required
    def searchFlights(current_user):
        flightId = str(request.args.get('flightId'))
        departureDate = str(request.args.get('departureDate'))
        fileDirectory = os.getcwd()
        jsonPath = os.path.join(fileDirectory, 'server',
                                'mock', 'mockSearch.json')
        with open(jsonPath, 'r') as flightDataFile:
            flightData = json.load(flightDataFile)
        print(flightData['data'])
        return flightData

    @app.route('/getFlights')
    def getFlights(current_user):
        # call db to get stuff
        return 'list of flights'

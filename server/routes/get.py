from flask import request
import json
import os


def getViews(app):
    @app.route('/searchFlights')
    def searchFlights():
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
    def getFlights():
        # call db to get stuff
        return 'list of flights'

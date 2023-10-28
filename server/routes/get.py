from flask import request

def getViews(app):
    @app.route('/searchFlights')
    def searchFlights():
        flightId = str(request.args.get('flightId'))
        departureDate = str(request.args.get('departureDate'))
        print(flightId)
        return flightId + departureDate
    
    @app.route('/getFlights')
    def getFlights():
        # call db to get stuff
        return 'list of flights'
    
    
from server.service.db import get_airport_by_id, get_flights_by_ids, get_flights_by_user, save_airport, save_flight, save_user_flight
from server.service.flight_api import search_by_ident_iata
from datetime import date, timedelta

def save(user_id, flight):
    origin_id = flight['origin']['code_iata']
    destination_id = flight['destination']['code_iata']
    origin = get_airport_by_id(origin_id)
    destination = get_airport_by_id(destination_id)
    if origin is None:
        origin_id = save_airport(flight['origin'])
    if destination is None:
        destination_id = save_airport(flight['destination'])
    flight['origin_id'] = origin_id
    flight['destination_id'] = destination_id
    flight_id = save_flight(flight)
    user_flight = dict({'user_id': user_id, 'flight_id': flight_id})
    save_user_flight(user_flight)
    return


def get_user_flights(user_id):
    user_flights = get_flights_by_user(user_id)
    flight_ids = [k["flight_id"] for k in user_flights]
    flights = get_flights_by_ids(flight_ids)
    now = date.today()
    to_update = []
    # if the flight is scheduled for departure and updated is either 15 minutes ago or has never been updated and is not completed
    for flight in flights:
        if flight['scheduled_off'] > now:
            if flight['updated_on'] is None or flight['updated_on'] < now - timedelta(minutes=15):
                if flight['progress_percent'] is not 100:
                    to_update.append(flight['fa_flight_id'])
                    flights.remove(flight)

    # update flights that need to be updated
    for flight_id in to_update:
        flight = search_by_ident_iata(flight_id)
        flights.append(flight)
        save_flight(flight)

    return flights

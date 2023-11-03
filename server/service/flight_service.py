from server.service.db import get_airport_by_id, save_airport, save_flight, save_user_flight


def save_flight(user_id, flight):
    origin_id = flight['origin']['code_iata']
    destination_id = flight['destination']['code_iata']
    origin = get_airport_by_id(origin_id)
    destination = get_airport_by_id(destination_id)
    if origin is None:
        save_airport(origin)
    if destination is None:
        save_airport(destination)
    flight['origin'] = origin_id
    flight['destination'] = destination_id
    save_flight(flight)
    user_flight = dict({'user_id': user_id, 'flight_id': flight['code_iata']})
    save_user_flight(user_flight)
    return

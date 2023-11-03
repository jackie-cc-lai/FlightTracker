from schema import Schema, And, Use, Optional, SchemaError


def flight_data_schema():
    schema = Schema({
        "ident": And(str, len),
        "ident_icao": And(str, len),
        "ident_iata": And(str, len),
        "fa_flight_id": And(str, len),
        "operator": And(str, len),
        "operator_icao": And(str, len),
        "operator_iata": And(str, len),
        "flight_number": And(str, len),
        "registration": And(str, len),
        "atc_ident": And(str, len),
        "inbound_fa_flight_id": And(str, len),
        "codeshares": [str],
        "codeshares_iata": [str],
        "blocked": bool,
        "diverted": bool,
        "cancelled": bool,
        "position_only": bool,
        "origin": {
            "code": And(str, len),
            "code_icao": And(str, len),
            "code_iata": And(str, len),
            "timezone": And(str, len),
            "name": And(str, len),
            "city": And(str, len),
            "airport_info_url": And(str, len),
            "object": object
        },
        "destination": {
            "code": And(str, len),
            "code_icao": And(str, len),
            "code_iata": And(str, len),
            "timezone": And(str, len),
            "name": And(str, len),
            "city": And(str, len),
            "airport_info_url": And(str, len),
            "object": object
        },
        "departure_delay": int,
        "arrival_delay": int,
        "scheduled_out": And(str, len),
        "scheduled_off": And(str, len),
        "scheduled_on": And(str, len),
        "scheduled_in": And(str, len),
        "aircraft_type": And(str, len),
        "object": object
    })
    return schema


def user_schema():
    schema = Schema({
        "id": str,
        "name": str,
        "email": str,

    })

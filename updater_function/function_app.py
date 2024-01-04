import logging
import azure.functions as func
from updater_function.service.db import get_flights, get_users_by_flights
from updater_function.service.api import search_flight
from datetime import date, timedelta
import os
import requests

app = func.FunctionApp()


@app.schedule(schedule="0 */15 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False)
def flight_updater(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
    flights = get_flights()
    for flight in flights:
        updated_flight = search_flight(flight['fa_flight_id'])

        if date(updated_flight['estimated_arrival']) < date.today() + timedelta(hours=1):
            to_notify_users = get_users_by_flights(
                updated_flight['fa_flight_id'])
            data = {
                "code_iata": flight['ident_iata'],
                "type": "Arrival",
                "users": to_notify_users,
            }
            requests.post(os.environ['NOTIFIER_URL'], data)
        if date(updated_flight['actual_departure'] is not None and updated_flight['actual_departure'] > date.today()):
            to_notify_users = get_users_by_flights(
                updated_flight['fa_flight_id'])
            data = {
                "code_iata": flight['ident_iata'],
                "type": "Departure",
                "users": to_notify_users,
            }
            requests.post(os.environ['NOTIFIER_URL'], data)

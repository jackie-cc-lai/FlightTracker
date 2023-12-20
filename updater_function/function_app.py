import logging
import azure.functions as func
from updater_function.service.db import get_flights
from updater_function.service.api import search_flight
from datetime import date, timedelta

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
            # send arrival notification
            
        if date(updated_flight['actual_departure'] is not None and updated_flight['actual_departure'] > date.today()):
            # send departure notification
        

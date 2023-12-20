import requests
import json
import os


def search_flight(ident_iata):
    api_key = os.environ["API_KEY"]
    url = os.environ['API_URL'] + '/flights/' + ident_iata
    headers = {
        "x-apikey": api_key,
        "Accept": "application/json; charset=UTF-8"
    }
    response = requests.get(url, headers=headers)
    return response.json()

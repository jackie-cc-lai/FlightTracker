import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def getData():
    apiKey = os.environ["API_KEY"]
    url = os.environ['APP_URL']


getData()

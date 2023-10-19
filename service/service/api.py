import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def getData():
    apiKey = os.environ["API_KEY"]
    appId = os.environ['APP_ID']
    url = os.environ['APP_URL']
    data = requests.get(url,)


getData()

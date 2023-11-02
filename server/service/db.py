import os
import psycopg2
from flask import Flask

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host=os.environ['DB_URL'],
                            database=os.environ['DB_NAME'],
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

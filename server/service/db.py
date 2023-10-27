import os
import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host=os.environ['DB_URL']
        database=os.environ['DB_NAME']
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

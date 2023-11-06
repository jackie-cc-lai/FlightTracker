import os
import psycopg2

from server.service.helper import create_dict, split_dict


def get_db_connection():
    conn = psycopg2.connect(host=os.environ['DB_URL'],
                            database=os.environ['DB_NAME'],
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


def get_user_by_id(id):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    db.execute('SELECT * FROM users WHERE users.id = %s;', (id,))
    user_data = db.fetchone()
    column_names = [desc[0] for desc in db.description]
    user = create_dict(user_data, column_names)
    db.close()
    db_connection.close()
    return user


def get_flights():
    db_connection = get_db_connection()
    db = db_connection.cursor()
    db.execute('SELECT * FROM flight_info WHERE flight_info.status IS NOT "scheduled" AND flight_info.progress_percent < 100;')
    flights_data = db.fetchall()
    column_names = [desc[0] for desc in db.description]
    flights = create_dict(flights_data, column_names)
    db.close()
    db_connection.close()
    return flights


def get_users_by_flights(flights):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    db.execute('SELECT * FROM user_flights WHERE flight_id IN %s',
               (flights['id']))
    user_flights_data = db.fetchall()
    column_names = [desc[0] for desc in db.description]
    user_flights = create_dict(user_flights_data, column_names)
    db.close()
    db_connection.close()
    return user_flights

import os
import psycopg2
from psycopg2 import sql
import logging
import json

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


def get_user_by_email(email):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    db.execute('SELECT * FROM users WHERE users.email = %s;', (email,))
    user_data = db.fetchone()
    column_names = [desc[0] for desc in db.description]
    user = create_dict(user_data, column_names)
    db.close()
    db_connection.close()
    return user


def get_flights_by_ids(ids):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    id_string = ', '.join(ids)
    db.execute(
        'SELECT * FROM flights WHERE flights.fa_flight_id IN (%s)', (id_string,))
    results = db.fetchall()
    column_names = [desc[0] for desc in db.description]
    flights = []
    for row in results:
        flight = create_dict(row, column_names)
        flights.append(flight)
    db.close()
    db_connection.close()
    return flights


def get_flights_by_user(user_id):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    db.execute('SELECT * FROM user_flights WHERE user_id = %s;', (user_id,))
    user_flight_data_rows = db.fetchall()
    column_names = [desc[0] for desc in db.description]
    user_flights = []
    for row in user_flight_data_rows:
        user_flight = create_dict(row, column_names)
        user_flights.append(user_flight)
    db.close()
    db_connection.close()
    return user_flights


def get_airport_by_id(id):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    db.execute('SELECT * FROM airports WHERE code_iata = %s;', (id,))
    airport_data = db.fetchone()
    if airport_data is None:
        return airport_data
    column_names = [desc[0] for desc in db.description]
    airport = create_dict(airport_data, column_names)
    db.close()
    db_connection.close()
    return airport


def save_flight(flight):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    try:
        db.execute('SELECT fa_flight_id from flights WHERE flights.fa_flight_id = %s;',
                   (flight['fa_flight_id'],))
        row_id = db.fetchone()
        if row_id is not None:
            print('Flight information exists within db already')
            return row_id
        else:
            db.execute(sql.SQL('INSERT INTO flights (fa_flight_id, operator, codeshares_iata, ident_iata, origin_id, destination_id, scheduled_off, flight_data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) returning fa_flight_id;'),
                       (flight['fa_flight_id'], flight['operator'], flight['codeshares_iata'], flight['ident_iata'], flight['origin_id'], flight['destination_id'], flight['scheduled_off'], json.dumps(flight)))
            db_connection.commit()
            flight_id = db.fetchone()[0]
            return flight_id
    except Exception as ex:
        print(ex)
        raise Exception('Cannot save flight information')
    finally:
        db.close()
        db_connection.close()


def save_airport(airport):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    try:
        db.execute("INSERT INTO airports(code_iata, code, code_icao, timezone, name, city) VALUES (%s, %s, %s, %s, %s, %s) returning code_iata;",
                   (airport['code_iata'], airport['code'], airport['code_icao'], airport['timezone'], airport['name'], airport['city']))
        row_id = db.fetchone()[0]
        db_connection.commit()

        return row_id
    except Exception as ex:
        print('exception occurred')
        print(type(ex))
        raise Exception('Cannot save airport information')
    finally:
        db.close()
        db_connection.close()


def save_user_flight(flight):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    try:
        db.execute('SELECT * from user_flights WHERE user_flights.flight_id = %s AND user_flights.user_id = %s;',
                   (flight['flight_id'], flight['user_id'],))
        row_id = db.fetchone()
        if row_id is not None:
            print('Flight has been saved for user already')
            return row_id
        else:
            db.execute('INSERT INTO user_flights(user_id, flight_id) VALUES (%s, %s) returning id',
                       (flight['user_id'], flight['flight_id'],))
            db_connection.commit()
            id = db.fetchone()[0]
            return id
    except Exception as ex:
        print(ex)
        raise Exception('Cannot save flight information')
    finally:
        db.close()
        db_connection.close()

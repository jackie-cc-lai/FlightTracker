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


def get_flights_by_user(user_id):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    db.execute('SELECT * FROM flight_info WHERE fa_flight_id = %s;', (email,))
    user_data = db.fetchone()
    column_names = [desc[0] for desc in db.description]
    user = create_dict(user_data, column_names)
    db.close()
    db_connection.close()
    return user


def get_airport_by_id(id):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    db.execute('SELECT * FROM airports WHERE code_iata = %s;', (id,))
    airport_data = db.fetchone()
    column_names = [desc[0] for desc in db.description]
    airport = create_dict(airport_data, column_names)
    db.close()
    db_connection.close()
    return airport


def save_flight(flight):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    [columns, values] = split_dict(flight)
    column_names = ', '.join(columns)
    values_string = ', '.join(values)
    try:
        db.execute('INSERT INTO flight_info(%s) VALUES (%s)',
                   (column_names, values_string, ))
        db.close()
        db_connection.close()
        return
    except Exception:
        print(Exception)
        raise Exception('Cannot save flight information')


def save_airport(airport):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    [columns, values] = split_dict(airport)
    column_names = ', '.join(columns)
    values_string = ', '.join(values)
    try:
        db.execute('INSERT INTO airports(%s) VALUES (%s)',
                   (column_names, values_string, ))
        db.close()
        db_connection.close()
        return
    except Exception:
        print(Exception)
        raise Exception('Cannot save airport information')


def save_user_flight(flight):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    [columns, values] = split_dict(flight)
    column_names = ', '.join(columns)
    values_string = ', '.join(values)
    try:
        db.execute('INSERT INTO flight_info(%s) VALUES (%s)',
                   (column_names, values_string, ))
        db.close()
        db_connection.close()
        return
    except Exception:
        print(Exception)
        raise Exception('Cannot save flight information')

from server.service.db import get_db_connection
import jwt
import os


def get_user(user_info):
    db_connection = get_db_connection()
    db = db_connection.cursor()
    email = None
    try:
        email = user_info['email']
    except Exception:
        pass
    id = None
    try:
        id = user_info['id']
    except Exception:
        pass
    if email is None and id is None:
        raise Exception('Cannot verify user')
    else:
        if email is None:
            db.execute('SELECT * FROM users WHERE users.id = %s;', (id,))
        else:
            db.execute('SELECT * FROM users WHERE users.email = %s;', (email,))
        user_data = db.fetchone()
        column_names = [desc[0] for desc in db.description]
        db.close()
        db_connection.close()
        user = dict()
        for i in range(len(column_names)):
            if column_names[i] == 'created_on':
                date = str(user_data[i])
                user[column_names[i]] = date
            else:
                user[column_names[i]] = user_data[i]
        return user


def generate_jwt(user):
    jwt_secret = os.environ['JWT_SECRET_KEY']
    return jwt.encode(user, jwt_secret, algorithm="HS256")


def verify_jwt(token):
    jwt_secret = os.environ['JWT_SECRET_KEY']
    values = jwt.decode(token, jwt_secret, algorithms=["HS256"])
    print(values)

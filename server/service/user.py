from server.service.db import get_db_connection, get_user_by_email, get_user_by_id
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
            return get_user_by_id(id)
        else:
            return get_user_by_email(email)

import psycopg2

from config import host, user, password, db_name


def connect():
    return psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

try:
     connection = connect()
except Exception as error:
    print("[ERROR] Failed to connect to the database: ", error)
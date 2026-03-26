import psycopg2
from config import host, db_name, user, password

def connect():
    return psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
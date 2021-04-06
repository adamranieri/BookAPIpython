from psycopg2 import connect
from psycopg2._psycopg import OperationalError


def create_connection():

    try:
        con = connect(
            database='bookDB',
            user='adam',
            password='gatorfan1',
            host='34.86.126.212',
            port='5432'
        )
        return con

    except OperationalError as e:
        print(f'{e}')
        return con

connection = create_connection()
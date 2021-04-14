from psycopg2 import connect
from psycopg2._psycopg import OperationalError
import os

def create_connection():

    try:
        con = connect(
            database = os.environ.get('database'), #bookDB
            user = os.environ.get('username'), #adam
            password = os.environ.get('password'), #pa$$word
            host = os.environ.get('host'), #00.00.000.000
            port = os.environ.get('port') #5432
        )
        return con

    except OperationalError as e:
        print(f'{e}')

connection = create_connection()
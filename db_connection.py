import psycopg2


def db_conn():
    # Connect to your postgres DB
    return psycopg2.connect(host='localhost', port='5432', database='incollege', user='postgres')


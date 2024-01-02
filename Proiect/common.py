import psycopg2


def connect_to_database():
    conn = psycopg2.connect(
        dbname="states_of_the_world",
        user="postgres",
        password="parola",
        host="localhost",
        port=5432)
    return conn


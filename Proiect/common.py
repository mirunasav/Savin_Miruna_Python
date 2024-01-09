import psycopg2


def connect_to_database():
    """Establishes a connection to the 'states_of_the_world' database.

    Returns:
        psycopg2.extensions.connection: A connection to the 'states_of_the_world' database.

    Raises:
        psycopg2.OperationalError: If there's an issue in connecting to the database.
    """
    conn = psycopg2.connect(
        dbname="states_of_the_world",
        user="postgres",
        password="parola",
        host="localhost",
        port=5432)
    return conn


import requests
from bs4 import BeautifulSoup
import psycopg2


def fetch_states(conn):
    url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
    response = requests.get(url)

    cursor = conn.cursor()

    if response.status_code != 200:
        raise Exception(f"Cannot access wikipedia list of countries; status code : {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})

    states = []
    try:
        for row in table.find_all('tr')[2:]:
            columns = row.find_all('td')
            state_name = columns[0].text.strip()
            states.append((state_name, ))
            print(state_name)

        insert_query = "Insert into states_of_the_world(name) values (%s)"
        cursor.executemany(insert_query, states)
        conn.commit()

    except psycopg2.Error as e:
        conn.rollback()
        print('Database errpr:', e)
    finally:
        cursor.close()
        conn.close()
    for state in states:
        print(state)


def connect_to_database():
    conn = psycopg2.connect(
        dbname="states_of_the_world",
        user="postgres",
        password="parola",
        host="localhost",
        port=5432)
    return conn

def main():
    try:
        conn  = connect_to_database()
        fetch_states(conn)
    except Exception as e:
        print(f"Exception: {e}")


main()

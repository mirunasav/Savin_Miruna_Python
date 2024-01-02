import re
from itertools import takewhile

import requests
from bs4 import BeautifulSoup
import psycopg2

from common import connect_to_database

indexPageURL = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
neighboursPageURL = 'https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_number_of_land_borders'


class State:
    def __init__(self, country_info):
        self.name = None
        self.capital = None
        self.population = 0
        self.population_density = float(0)
        self.area = 0
        self.language = None
        self.time_zone = None
        self.political_regime = None

        for key, value in country_info.items():
            if key == 'Name':
                self.name = value
            if key == 'Capital':
                self.capital = value
            if key == 'Population':
                self.population = value
            if key == 'Population density':
                self.population_density = value
            if key == 'Area':
                self.area = value
            if key == 'Language':
                self.language = value
            if key == 'Time zone':
                self.time_zone = value
            if key == 'Political regime':
                self.political_regime = value

    def print(self):
        print(f'State:{self.name},'
              f' Capital : {self.capital},'
              f' Population : {self.population},'
              f' Population density : {self.population_density} / square km,'
              f' Total area: {self.area} square km,'
              f' Language : {self.language},'
              f' Time zone: {self.time_zone},'
              f' Political regime: {self.political_regime}')


def fetch_states(conn):
    url = indexPageURL
    response = requests.get(url)

    cursor = conn.cursor()

    if response.status_code != 200:
        raise Exception(f"Cannot access wikipedia list of countries; status code : {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})

    states = []

    for row in table.find_all('tr')[2:]:
        columns = row.find_all('td')
        state_name = columns[0].text.strip()
        state_link = columns[0].find('a')['href']
        state_url = f'https://en.wikipedia.org{state_link}'
        state_info = fetch_state_info(state_name, state_url)
        states.append(state_info)

    try:
        for state in states:
            insert_query = "insert into states_of_the_world(name,capital,population,population_density,area,language," \
                           "time_zone,political_regime)" \
                           "values(%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (state.name, state.capital, state.population, state.population_density,
                                          state.area, state.language, state.time_zone, state.political_regime))
            conn.commit()

    except psycopg2.Error as e:
        conn.rollback()
        print('Database error:', e)
    finally:
        cursor.close()
        conn.close()


def fetch_state_neighbours(conn):
    url = neighboursPageURL
    response = requests.get(url)

    cursor = conn.cursor()

    if response.status_code != 200:
        raise Exception(f"Cannot access wikipedia list of countries; status code : {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})

    states_and_neighbours = {}
    for row in table.find_all('tr')[2:]:
        columns = row.find_all('td')
        state_letters = takewhile(lambda x: not x.isdigit() and not is_character_parantheses(x) and x != ',',
                                    columns[0].text.strip().lower())
        state_name = ''.join(state_letters)
        neighbours_data = columns[5].find_all('a')

        neighbours = []

        for a_tag in neighbours_data:
            text = a_tag.get_text(strip=True)
            if '[' not in text and ']' not in text:
                neighbours.append(text)

        neighbours_string = ', '.join(neighbours)
        states_and_neighbours[state_name] = neighbours_string

    try:
        for state, neighbours in states_and_neighbours.items():
            update_query = "UPDATE states_of_the_world SET neighbours = %s WHERE LOWER(name) = %s"
            cursor.execute(update_query, (neighbours, state))
        conn.commit()

    except psycopg2.Error as e:
        conn.rollback()
        print('Database error:', e)
    finally:
        cursor.close()
        conn.close()

    return states_and_neighbours

def is_character_part_of_number(x):
    return x.isdigit() or x == ',' or x == '.'

def is_character_parantheses(x):
    return x == '(' or x == ')' or x == ']' or x == '[' or x == '}' or x == '{'

def fetch_state_info(state_name, state_url):
    response = requests.get(state_url)
    country_info = {'Name': state_name}

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        info_table = soup.find('table', {'class': 'infobox'})

        if info_table:
            rows = info_table.find_all('tr')
            for row in rows:
                header = row.find('th')
                if header:
                    header_text = header.get_text(strip=True)
                    if 'capital' in header_text.lower():
                        capital_letters = takewhile(lambda x: not x.isdigit() and not is_character_parantheses(x), row.find('td').get_text(strip=True))
                        country_info['Capital'] = ''.join(capital_letters)
                        continue

                    if header_text.lower() == 'population':
                        population_row = row.find_next_sibling('tr')
                        population_data = takewhile(is_character_part_of_number,
                                                    population_row.find('td').get_text(strip=True).split(' ')[0])
                        country_info['Population'] = int(''.join(population_data).replace(',', '').replace('.', ''))
                        continue

                    if 'density' in header_text.lower():
                        population_density = ''.join(takewhile(is_character_part_of_number,
                                                               row.find('td').get_text(strip=True)))
                        country_info['Population density'] = '{:.2f}'.format(float(population_density.replace(',', '')))
                        continue

                    if header_text.lower() == 'area':
                        total_area_row = row.find_next_sibling('tr')
                        total_area = takewhile(is_character_part_of_number,
                                               total_area_row.find('td').get_text(strip=True).split(' ')[0])
                        country_info['Area'] = int(''.join(total_area).replace(',', '').replace('.', ''))
                        continue

                    if 'official language' in header_text.lower().replace('\xa0', ' '):
                        languages = row.find('td').get_text(strip=True)
                        if languages:
                            matching_regex = re.match('[A-Z][a-z]*( [A-Z][a-z]*)*', languages)
                            if matching_regex is not None:
                                country_info['Language'] = matching_regex.group()
                        else:
                            country_info['Language'] = None
                        continue

                    if 'time zone' in header_text.lower():
                        time_zone = takewhile(lambda x: not is_character_parantheses(x) and x != ' ' and x != ';' and x != ',', row.find('td').get_text(strip=True))
                        country_info['Time zone'] = ''.join(time_zone)
                        continue

                    if header_text.lower() == 'government':
                        political_regime = takewhile(lambda x: not x.isdigit() and not is_character_parantheses(x), row.find('td').get_text(strip=False))
                        country_info['Political regime'] = ''.join(political_regime)

    return State(country_info)


def main():
  #  fetch_states(connect_to_database())
    fetch_state_neighbours(connect_to_database())


main()

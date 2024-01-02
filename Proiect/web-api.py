from collections import OrderedDict

from flask import Flask, jsonify, request
from common import connect_to_database

app = Flask(__name__)
app.json.sort_keys = False

class State:
    def __init__(self, *args, **kwargs):
        self.id = None
        self.name = None
        self.capital = None
        self.population = 0
        self.population_density = float(0)
        self.area = 0
        self.language = None
        self.time_zone = None
        self.political_regime = None
        self.neighbours = None

        if len(args) == 10:
            self.id, self.name, self.capital, self.population, self.population_density, self.area, \
                self.language, self.time_zone, self.political_regime, self.neighbours = args

        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key.lower().replace(' ', '_'), value)


# get all countries and afferent info
@app.route('/countries', methods=['GET'])
def get_countries():
    language = request.args.get('language')
    time_zone = request.args.get('time-zone')
    government = request.args.get('political-regime')

    query = "SELECT * FROM states_of_the_world WHERE TRUE"
    params = []

    if language:
        query += " AND  LOWER(language) = %s"
        params.append(language.lower())

    if time_zone:
        query += " AND LOWER(time_zone) = %s"
        params.append(time_zone.lower())

    if government:
        query += " AND LOWER(political_regime) = %s"
        params.append(government.lower())

    query += " ORDER BY id ASC"
    print(f"Database Query: {query} with parameters {params}")

    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(query, params)
    countries_data = cursor.fetchall()
    cursor.close()
    conn.close()

    country_objects = []
    for country_data in countries_data:
        country = State(*country_data)
        country_objects.append(country)

    country_dicts = [
        {
            "id": country.id,
            "name": country.name,
            "capital": country.capital,
            "population": country.population,
            "population_density": country.population_density,
            "area": country.area,
            "language": country.language,
            "neighbours": country.neighbours,
            "time_zone": country.time_zone,
            "political_regime": country.political_regime
        }
        for country in country_objects
    ]
    return country_dicts

# get all countries and their capitals
@app.route('/countries/capitals', methods=['GET'])
def get_countries_capitals():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, capital FROM states_of_the_world")
    capitals_data = cursor.fetchall()
    cursor.close()
    conn.close()

    capitals = [{'name': name, 'capital': capital} for name, capital in capitals_data]
    return jsonify(capitals)


# get all countries and their population densities
@app.route('/countries/population-density', methods=['GET'])
def get_countries_population_densities():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population_density FROM states_of_the_world")
    capitals_data = cursor.fetchall()
    cursor.close()
    conn.close()

    capitals = [{'name': name, 'population_density': population_density} for name, population_density in capitals_data]
    return jsonify(capitals)


@app.route('/countries/population-density/top-10', methods=['GET'])
def get_top_10_countries_by_population_density():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population_density FROM states_of_the_world ORDER BY population_density DESC LIMIT 10")
    top_10_population_density = cursor.fetchall()
    cursor.close()
    conn.close()

    top_10 = [{'name': name, 'population_density': population_density} for name, population_density in top_10_population_density]
    return jsonify(top_10)



@app.route('/countries/population-density/last-10', methods=['GET'])
def get_last_10_countries_by_population_density():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population_density FROM states_of_the_world ORDER BY population_density ASC LIMIT 10")
    last_10_population_density = cursor.fetchall()
    cursor.close()
    conn.close()

    last_10 = [{'name': name, 'population_density': population_density} for name, population_density in last_10_population_density]
    return jsonify(last_10)


# get all countries and their population
@app.route('/countries/population', methods=['GET'])
def get_countries_population():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population FROM states_of_the_world")
    population_data = cursor.fetchall()
    cursor.close()
    conn.close()

    population = [{'name': name, 'population': population} for name, population in population_data]
    return jsonify(population)


@app.route('/countries/population/top-10', methods=['GET'])
def get_top_10_countries_by_population():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population FROM states_of_the_world ORDER BY population DESC LIMIT 10")
    top_10_population = cursor.fetchall()
    cursor.close()
    conn.close()

    top_10 = [{'name': name, 'population': population} for name, population in top_10_population]
    return jsonify(top_10)


@app.route('/countries/population/last-10', methods=['GET'])
def get_last_10_countries_by_population():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population FROM states_of_the_world ORDER BY population ASC LIMIT 10")
    last_10_population = cursor.fetchall()
    cursor.close()
    conn.close()

    last_10 = [{'name': name, 'population': population} for name, population in last_10_population]
    return jsonify(last_10)


# get all countries and their area
@app.route('/countries/area', methods=['GET'])
def get_countries_area():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, area FROM states_of_the_world")
    area_data = cursor.fetchall()
    cursor.close()
    conn.close()

    area = [{'name': name, 'area': area} for name, area in area_data]
    return jsonify(area)


@app.route('/countries/area/top-10', methods=['GET'])
def get_top_10_countries_by_area():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, area FROM states_of_the_world ORDER BY area DESC LIMIT 10")
    top_10_area = cursor.fetchall()
    cursor.close()
    conn.close()

    top_10 = [{'name': name, 'area': area} for name, area in top_10_area]
    return jsonify(top_10)


@app.route('/countries/area/last-10', methods=['GET'])
def get_last_10_countries_by_area():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, area FROM states_of_the_world ORDER BY area ASC LIMIT 10")
    last_10_area = cursor.fetchall()
    cursor.close()
    conn.close()

    last_10 = [{'name': name, 'area': area} for name, area in last_10_area]
    return jsonify(last_10)


# get all countries and their language
@app.route('/countries/language', methods=['GET'])
def get_countries_language():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, language FROM states_of_the_world")
    language_data = cursor.fetchall()
    cursor.close()
    conn.close()

    language = [{'name': name, 'language': language} for name, language in language_data]
    return jsonify(language)


# get all countries and their time zone
@app.route('/countries/time-zone', methods=['GET'])
def get_countries_time_zone():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, time_zone FROM states_of_the_world")
    time_zone_data = cursor.fetchall()
    cursor.close()
    conn.close()

    time_zone = [{'name': name, 'time_zone': time_zone} for name, time_zone in time_zone_data]
    return jsonify(time_zone)


# get all countries and their political regime
@app.route('/countries/political-regime', methods=['GET'])
def get_countries_political_regime():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, political_regime FROM states_of_the_world")
    political_regime_data = cursor.fetchall()
    cursor.close()
    conn.close()

    political_regime = [{'name': name, 'political_regime': political_regime} for name, political_regime in political_regime_data]
    return jsonify(political_regime)


# get all countries and their neighbours
@app.route('/countries/neighbours', methods=['GET'])
def get_countries_neighbours():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, neighbours FROM states_of_the_world WHERE neighbours IS NOT NULL ORDER BY id ASC")
    neighbours_data = cursor.fetchall()
    cursor.close()
    conn.close()

    neighbours = [{'name': name, 'neighbours': neighbours} for name, neighbours in neighbours_data]
    return jsonify(neighbours)


if __name__ == "__main__":
    app.run(debug=True)

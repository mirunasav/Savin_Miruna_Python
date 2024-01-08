from flask import Flask, jsonify, request

from common import connect_to_database

app = Flask(__name__)
app.json.sort_keys = False


class State:
    """Represents a state with various attributes."""

    def __init__(self, *args):
        """Initialize State object with attributes.

               Args:
                   *args: Accepts 10 arguments in the following order:
                       id (int): The ID of the state.
                       name (str): The name of the state.
                       capital (str): The capital city of the state.
                       population (int): The population of the state.
                       population_density (float): The population density of the state.
                       area (int): The area of the state.
                       language (str): The primary language spoken in the state.
                       time_zone (str): The time zone of the state.
                       political_regime (str): The type of political regime in the state.
                       neighbours (str): The neighbouring countries of the state.
               """
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

        self.id, self.name, self.capital, self.population, self.population_density, self.area, \
        self.language, self.time_zone, self.political_regime, self.neighbours = args


@app.route('/countries', methods=['GET'])
def get_countries():
    """Retrieve information about countries based on optional query parameters.

     This route retrieves information about countries from the 'states_of_the_world' table
     in the database based on optional query parameters:
     - 'language': Filters countries by the specified language.
     - 'time-zone': Filters countries by the specified time zone.
     - 'political-regime': Filters countries by the specified political regime.
     If no query parameters are provided, all the countries will be retrieved from the database
     (no filtering would be applied)

     Returns:
         list: A list of dictionaries containing all the information about countries based on the query parameters.
     """
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


@app.route('/countries/capitals', methods=['GET'])
def get_countries_capitals():
    """Retrieve all countries and their capitals from the database.

        This route fetches data from the 'states_of_the_world' table in the database,
        specifically the 'name' (country name) and 'capital' columns, and returns a JSON response
        containing a list of dictionaries, each containing the country name and its corresponding capital.

        Returns:
            Flask.Response: A JSON response containing a list of dictionaries with country names and capitals.
        """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, capital FROM states_of_the_world")
    capitals_data = cursor.fetchall()
    cursor.close()
    conn.close()

    capitals = [{'name': name, 'capital': capital} for name, capital in capitals_data]
    return jsonify(capitals)


@app.route('/countries/population-density', methods=['GET'])
def get_countries_population_densities():
    """Retrieve all countries and their population densities from the database.

          This route fetches data from the 'states_of_the_world' table in the database,
          specifically the 'name' (country name) and 'population-density' columns, and returns a JSON response
          containing a list of dictionaries, each containing the country name and its corresponding population density.

          Returns:
              Flask.Response: A JSON response containing a list of dictionaries
              with country names and population densities.
          """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population_density FROM states_of_the_world order by id")
    capitals_data = cursor.fetchall()
    cursor.close()
    conn.close()

    capitals = [{'name': name, 'population_density': population_density} for name, population_density in capitals_data]
    return jsonify(capitals)


@app.route('/countries/population-density/top-10', methods=['GET'])
def get_top_10_countries_by_population_density():
    """Retrieve the top 10 countries by population density.

     This route fetches data from the 'states_of_the_world' table in the database
     and retrieves the names and population densities of the top 10 countries
     ordered by population density in descending order.

     Returns:
         Flask.Response: A JSON response containing a list of dictionaries with names and population densities
         of the top 10 countries by population density.
     """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population_density FROM states_of_the_world ORDER BY population_density DESC LIMIT 10")
    top_10_population_density = cursor.fetchall()
    cursor.close()
    conn.close()

    top_10 = [{'name': name, 'population_density': population_density} for name, population_density in
              top_10_population_density]
    return jsonify(top_10)


@app.route('/countries/population-density/last-10', methods=['GET'])
def get_last_10_countries_by_population_density():
    """Retrieve the last 10 countries by population density.

     This route fetches data from the 'states_of_the_world' table in the database
     and retrieves the names and population densities of the last 10 countries
     ordered by population density in ascending order.

     Returns:
         Flask.Response: A JSON response containing a list of dictionaries with names and population densities
         of the last 10 countries by population density.
     """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population_density FROM states_of_the_world ORDER BY population_density ASC LIMIT 10")
    last_10_population_density = cursor.fetchall()
    cursor.close()
    conn.close()

    last_10 = [{'name': name, 'population_density': population_density} for name, population_density in
               last_10_population_density]
    return jsonify(last_10)


@app.route('/countries/population', methods=['GET'])
def get_countries_population():
    """Retrieve all countries and their populations.

       This route fetches data from the 'states_of_the_world' table in the database
       and retrieves the names and populations of all countries ordered by ID.

       Returns:
           Flask.Response: A JSON response containing a list of dictionaries with country names and populations.
       """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population FROM states_of_the_world order by id")
    population_data = cursor.fetchall()
    cursor.close()
    conn.close()

    population = [{'name': name, 'population': population} for name, population in population_data]
    return jsonify(population)


@app.route('/countries/population/top-10', methods=['GET'])
def get_top_10_countries_by_population():
    """Retrieve the top 10 countries by population.

     This route fetches data from the 'states_of_the_world' table in the database
     and retrieves the names and populations of the top 10 countries ordered by population in descending order.

     Returns:
         Flask.Response: A JSON response containing a list of dictionaries with names and populations
         of the top 10 countries by population.
     """
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
    """Retrieve the last 10 countries by population.

      This route fetches data from the 'states_of_the_world' table in the database
      and retrieves the names and populations of the last 10 countries ordered by population in ascending order.

      Returns:
          Flask.Response: A JSON response containing a list of dictionaries with names and populations
          of the last 10 countries by population.
      """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, population FROM states_of_the_world ORDER BY population ASC LIMIT 10")
    last_10_population = cursor.fetchall()
    cursor.close()
    conn.close()

    last_10 = [{'name': name, 'population': population} for name, population in last_10_population]
    return jsonify(last_10)


@app.route('/countries/area', methods=['GET'])
def get_countries_area():
    """Retrieve all countries and their areas.

        This route fetches data from the 'states_of_the_world' table in the database
        and retrieves the names and areas of all countries ordered by ID.

        Returns:
            Flask.Response: A JSON response containing a list of dictionaries with country names and areas.
        """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, area FROM states_of_the_world order by id")
    area_data = cursor.fetchall()
    cursor.close()
    conn.close()

    area = [{'name': name, 'area': area} for name, area in area_data]
    return jsonify(area)


@app.route('/countries/area/top-10', methods=['GET'])
def get_top_10_countries_by_area():
    """Retrieve the top 10 countries by area.

       This route fetches data from the 'states_of_the_world' table in the database
       and retrieves the names and areas of the top 10 countries ordered by area in descending order.

       Returns:
           Flask.Response: A JSON response containing a list of dictionaries with names and areas
           of the top 10 countries by area.
       """
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
    """Retrieve the last 10 countries by area.

       This route fetches data from the 'states_of_the_world' table in the database
       and retrieves the names and areas of the last 10 countries ordered by area in ascending order.

       Returns:
           Flask.Response: A JSON response containing a list of dictionaries with names and areas
           of the last 10 countries by area.
       """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, area FROM states_of_the_world ORDER BY area ASC LIMIT 10")
    last_10_area = cursor.fetchall()
    cursor.close()
    conn.close()

    last_10 = [{'name': name, 'area': area} for name, area in last_10_area]
    return jsonify(last_10)


@app.route('/countries/language', methods=['GET'])
def get_countries_language():
    """Retrieve all countries and their languages.

      This route fetches data from the 'states_of_the_world' table in the database
      and retrieves the names and languages spoken in all countries ordered by ID.

      Returns:
          Flask.Response: A JSON response containing a list of dictionaries with country names and languages spoken.
      """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, language FROM states_of_the_world order by id")
    language_data = cursor.fetchall()
    cursor.close()
    conn.close()

    language = [{'name': name, 'language': language} for name, language in language_data]
    return jsonify(language)


@app.route('/countries/time-zone', methods=['GET'])
def get_countries_time_zone():
    """Retrieve all countries and their time zones.

       This route fetches data from the 'states_of_the_world' table in the database
       and retrieves the names and time zones of all countries ordered by ID.

       Returns:
           Flask.Response: A JSON response containing a list of dictionaries with country names and their time zones.
       """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, time_zone FROM states_of_the_world order by id")
    time_zone_data = cursor.fetchall()
    cursor.close()
    conn.close()

    time_zone = [{'name': name, 'time_zone': time_zone} for name, time_zone in time_zone_data]
    return jsonify(time_zone)


@app.route('/countries/political-regime', methods=['GET'])
def get_countries_political_regime():
    """Retrieve all countries and their political regimes.

       This route fetches data from the 'states_of_the_world' table in the database
       and retrieves the names and political regimes of all countries ordered by ID.

       Returns:
           Flask.Response: A JSON response containing a list of dictionaries with country names and their political regimes.
       """
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name, political_regime FROM states_of_the_world order by id")
    political_regime_data = cursor.fetchall()
    cursor.close()
    conn.close()

    political_regime = [{'name': name, 'political_regime': political_regime} for name, political_regime in
                        political_regime_data]
    return jsonify(political_regime)


# get all countries and their neighbours
@app.route('/countries/neighbours', methods=['GET'])
def get_countries_neighbours():
    """Retrieve all countries and their neighbours.

          This route fetches data from the 'states_of_the_world' table in the database
          and retrieves the names and neighbouring countries of all countries that have neighbours specified, ordered by ID.

          Returns:
              Flask.Response: A JSON response containing a list of dictionaries with country names and their neighbours.
          """
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

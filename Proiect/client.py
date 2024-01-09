import requests

BASE_URL = 'http://127.0.0.1:5000/countries'


def get_request(url):
    """
       Sends a GET request to the specified URL and prints the JSON response,
        with each key-value pair on a separate line.

       Args:
           url (str): The URL to send the GET request to.
       """
    response = requests.get(url)

    if not response.ok:
        print("An error occurred")
        return

    for country in response.json():
        for key, value in country.items():
            print(f'{key} : {value}')
        print()


def get_countries():
    """Makes a request to get all countries and their properties and prints the response"""
    get_request(f'{BASE_URL}')


def get_countries_capitals():
    """Makes a request to get all countries and their capitals and prints the response"""
    get_request(f'{BASE_URL}/capitals')


def get_countries_population_densities():
    """Makes a request to get all countries and their population densities
     and prints the response"""
    get_request(f'{BASE_URL}/population-density')


def get_top_10_countries_by_population_density():
    """Makes a request to get top 10 countries ordered by population density
     prints the response"""
    get_request(f'{BASE_URL}/population-density/top-10')


def get_last_10_countries_by_population_density():
    """Makes a request to the last 10 countries ordered by population density
     and prints the response"""
    get_request(f'{BASE_URL}/population-density/last-10')


def get_countries_population():
    """Makes a request to get all countries and their populations and prints the response"""
    get_request(f'{BASE_URL}/population')


def get_top_10_countries_by_population():
    """Makes a request to get top 10 countries ordered by population
      and prints the response"""
    get_request(f'{BASE_URL}/population/top-10')


def get_last_10_countries_by_population():
    """Makes a request to get the last 10 countries ordered by population and prints the response"""

    get_request(f'{BASE_URL}/population/last-10')


def get_countries_area():
    """Makes a request to get all countries and their ares and prints the response"""

    get_request(f'{BASE_URL}/area')


def get_top_10_countries_by_area():
    """Makes a request to get top 10 countries ordered by area
     and prints the response"""

    get_request(f'{BASE_URL}/area/top-10')


def get_last_10_countries_by_area():
    """Makes a request to get last 10 countries ordered by area
    and prints the response"""
    get_request(f'{BASE_URL}/area/last-10')


def get_countries_language():
    """Makes a request to get all countries and their language and prints the response"""
    get_request(f'{BASE_URL}/language')


def get_countries_time_zone():
    """Makes a request to get all countries and their time zone and prints the response"""
    get_request(f'{BASE_URL}/time-zone')


def get_countries_political_regime():
    """Makes a request to get all countries and their political regime and prints the response"""
    get_request(f'{BASE_URL}/political-regime')


def get_countries_neighbours():
    """Makes a request to get all countries and their neighbours and prints the response"""
    get_request(f'{BASE_URL}/neighbours')


def get_countries_gmt2():
    """Makes a request to get all countries on gmt+2 time zone
     and prints the response"""
    get_request(f'{BASE_URL}?time-zone=utc%2B2')


def get_countries_english():
    """Makes a request to get all countries that speak English
     and prints the response"""
    get_request(f'{BASE_URL}?language=English')


def get_countries_federal_pres_republic():
    """Makes a request to get all countries with a federal presidential republic political regime
     and prints the response"""
    get_request(f'{BASE_URL}?political-regime=federal%20presidential%20republic')


def map_request_number_to_api_call():
    """
       Maps numeric input to corresponding API call functions.

       Returns:
           dict: A dictionary mapping numeric input strings to corresponding API call functions.
       """

    request_map = {
        "1": get_countries,
        "2": get_countries_capitals,
        "3": get_countries_population,
        "4": get_countries_language,
        "5": get_countries_population_densities,
        "6": get_countries_area,
        "7": get_countries_time_zone,
        "8": get_countries_political_regime,
        "9": get_countries_neighbours,
        "10": get_top_10_countries_by_population,
        "11": get_top_10_countries_by_area,
        "12": get_top_10_countries_by_population_density,
        "13": get_countries_gmt2,
        "14": get_countries_english,
        "15": get_countries_federal_pres_republic
    }

    return request_map


def print_options():
    """
       Displays a list of options for API calls and prompts user for selection.

       Returns:
           str: The user's choice for API call.
       """
    return input("1 : get all countries\n"
                 "2 : get all countries and capitals\n"
                 "3 : get all countries and their populations\n"
                 "4 : get all countries and their language\n"
                 "5 : get all countries and their population density\n"
                 "6 : get all countries and their area\n"
                 "7 : get all countries and their time zone\n"
                 "8 : get all countries and their political regime\n"
                 "9 : get all countries and their neighbours\n"
                 "10 : get top 10 countries by population\n"
                 "11 : get top 10 countries by area\n"
                 "12 : get top 10 countries by population density\n"
                 "13: get all countries on gmt+2\n"
                 "14 : get all countries speaking English\n"
                 "15: get all countries with a certain political regime\n")


def main():
    """
       Main function to execute API calls based on user input.
       The user can choose between a predefined list of requests or writing his own request.
       """
    request_map = map_request_number_to_api_call()
    while True:
        client_input = input("Do you want to call a predefined route or write your own GET request? 1/2 ")
        if client_input == '1':
            request_number = print_options()
            response = request_map.get(request_number, None)
            if response is None:
                print("invalid request number")
            else:
                response()
        elif client_input == '2':
            route = input("write your request URL: /countries")
            get_request(f'{BASE_URL}{route}')
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()

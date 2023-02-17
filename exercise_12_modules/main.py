"""
This is a module docstring.

Run the code by typing 'python main.py --city "City Name"'
in the terminal.
"""

import sys
import pytz
from datetime import datetime
import argparse  # Deze import toegevoegd

from cities import CITIES


def get_city(city):
    """
    Loop through all items in cities.py and return the city that
    the user inputted.

    arg1 = city name
    """
    for city_data in CITIES:
        if city_data['city'].lower() == city.lower():
            return city_data
    # return None # Lijkt erop dat dit niet nodig is


def get_time(timezone):
    """
    Return the current time in a specific timezone.

    arg1 = timezone name
    """
    return datetime.now().astimezone(
        pytz.timezone(timezone)
        ).strftime("%H:%M:%S")


def parse_args():
    """
    Use argparse to obtain an understandable CLI.
    """
    parser = argparse.ArgumentParser('Enter a city to get its local time')
    parser.add_argument('-c', '--city', type=str,
                        help='The city name in English',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    """
    Use the previous functions to calculate the current local time'
    in a given city, or return a message when no data was found.
    """
    args = parse_args()
    city_data = get_city(args.city)
    print('---Result---')
    if city_data is not None:
        time = get_time(city_data['timezone'])
        print(f'It is currently {time} in {city_data["city"]}, {city_data["country"]}')
    else:
        print(f'Unfortunately no data was found for city: {sys.argv[1]}')


if __name__ == '__main__':
    main()

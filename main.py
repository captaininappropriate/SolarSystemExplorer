# Title: Solar System Explorer
# Description: A Python program that allows users to explore information about the planets in our solar system.
# Requires: Python 3.x and an API key from a The Solar System Open Data (https://api.le-systeme-solaire.net/en/) which is stored in constants.py
# Author: Greg Nimmo
# Date: 06/01/2026
# Version: 1.0
# License: GNU General Public License v3.0
# GitHub: https://github.com/captaininappropriate/SolarSystemExplorer

# import required modules
from constants import API_KEY
import json
import requests


def greeting():
    # Display greeting message
    print("Welcome to the Solar System Explorer!")
    print("Explore information about the planets in our solar system.\n")


def fetch_planet_data(planet_name):
    # Fetch planet data from the API
    bearer_token = API_KEY
    headers = {"Authorization": f"Bearer {bearer_token}"}
    url = f"https://api.le-systeme-solaire.net/rest/bodies/{planet_name.lower()}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for {planet_name}. Please check the planet name and try again.")
        return None


def menu():
    # Display menu options
    while True:
        print("Menu:")
        print("1. View Planet Information")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        # Handle user choice
        # Using match-case for Python 3.10+
        match choice:
            case '1':
                planet_name = input("Enter the name of a planet or moon (e.g., Earth, Euanthe): ")
                planet_data = fetch_planet_data(planet_name)
                if planet_data:
                    print(json.dumps(planet_data, indent=4))
            case '2':
                print("Exiting the Solar System Explorer. Goodbye!")
                exit(0)
            case _:
                print("Invalid choice. Please try again.")
                menu()


menu()


#if __name__ == "__main__":
#    # Check if API key is present
#    API_KEY = API_KEY  # Use the imported API key from constants.py
#    if not API_KEY:
#        print("\nERROR: API Key is missing. Please set your API key in constants.py")
#        exit(1)
#    else:
#        print("API Key loaded successfully.\n")
#        greeting()

if __name__ == "__main__":
    greeting()

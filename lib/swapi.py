import requests
from dataclasses import asdict, dataclass


class SwapiAPI:
    """
    swapi.info/api/films
    swapi.info/api/people
    swapi.info/api/planets
    swapi.info/api/species
    swapi.info/api/vehicles
    swapi.info/api/starships
    """

    def __init__(self):
        self.base_url = "https://swapi.info/api"

    def get_films_data(self, index: int = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/films"
        else:
            url = f"{self.base_url}/films/{index}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_people_data(self, index: int = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/people"
        else:
            url = f"{self.base_url}/people/{index}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_planets_data(self, index: int = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/planets"
        else:
            url = f"{self.base_url}/planets/{index}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_species_data(self, index: int = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/species"
        else:
            url = f"{self.base_url}/species/{index}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_vehicles_data(self, index: int = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/vehicles"
        else:
            url = f"{self.base_url}/vehicles/{index}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_starships_data(self, index: int = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/starships"
        else:
            url = f"{self.base_url}/starships/{index}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

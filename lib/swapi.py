from lib.util import Paginator
from typing import Optional


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
        self.paginator = Paginator()

    def get_films_data(self, index: Optional[int] = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/films"
        else:
            url = f"{self.base_url}/films/{index}/"
        return self.paginator.fetch_all(url)

    def get_people_data(self, index: Optional[int] = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/people"
        else:
            url = f"{self.base_url}/people/{index}/"
        return self.paginator.fetch_all(url)

    def get_planets_data(self, index: Optional[int] = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/planets"
        else:
            url = f"{self.base_url}/planets/{index}/"
        return self.paginator.fetch_all(url)

    def get_species_data(self, index: Optional[int] = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/species"
        else:
            url = f"{self.base_url}/species/{index}/"
        return self.paginator.fetch_all(url)

    def get_vehicles_data(self, index: Optional[int] = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/vehicles"
        else:
            url = f"{self.base_url}/vehicles/{index}/"
        return self.paginator.fetch_all(url)

    def get_starships_data(self, index: Optional[int] = None):
        if isinstance(index, int) and index < 0:
            raise ValueError("Index must be positive")
        if index is None:
            url = f"{self.base_url}/starships"
        else:
            url = f"{self.base_url}/starships/{index}/"
        return self.paginator.fetch_all(url)

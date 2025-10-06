import logging

import pytest

from lib.swapi import SwapiAPI

logger = logging.getLogger(__name__)

swapi_api = SwapiAPI()


class TestSwapi:

    @pytest.mark.parametrize("film_id, expected", [(6, 20)])
    def test_get_how_many_species_in_film(self, film_id, expected):
        """
        Q1 有多少不同種族的人出現在第六部？
        """
        films = swapi_api.get_films_data(film_id)
        assert len(films[0]["species"]) == expected

    def test_sort_by_episode(self):
        """
        Q2 請依據電影集數去排序電影名字
        """
        EXPECTED_TITLES = [
            "The Phantom Menace",
            "Attack of the Clones",
            "Revenge of the Sith",
            "A New Hope",
            "The Empire Strikes Back",
            "Return of the Jedi",
        ]
        films = swapi_api.get_films_data()
        sorted_films = sorted(films, key=lambda x: x["episode_id"])
        result = [film["title"] for film in sorted_films]
        assert set(result) == set(
            EXPECTED_TITLES
        ), f"Expected {EXPECTED_TITLES} but got {result}"

    def test_vehicles_with_power_over_1000(self):
        """
        Q3 請幫我挑出電影裡所有的車輛，馬力超過１０００的。
        """
        EXPECTED_FAST_VEHICLE_NAMES = [
            "Geonosian starfighter",
            "Storm IV Twin-Pod cloud car",
            "TIE/IN interceptor",
            "T-16 skyhopper",
            "TIE/LN starfighter",
            "Vulture Droid",
            "Droid tri-fighter",
        ]
        vehicles = swapi_api.get_vehicles_data()
        result = []
        for vehicle in vehicles:
            try:
                if int(vehicle["max_atmosphering_speed"]) > 1000:
                    result.append(vehicle["name"])
            except ValueError:
                pass
        assert set(result) == set(
            EXPECTED_FAST_VEHICLE_NAMES
        ), f"Expected {EXPECTED_FAST_VEHICLE_NAMES} but got {result}"

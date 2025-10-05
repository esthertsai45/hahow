import json
import logging

from lib.swapi import SwapiAPI

logger = logging.getLogger(__name__)

swapi_api = SwapiAPI()

# Q1 有多少不同種族的人出現在第六部？


def get_how_many_species_in_film(film_id: int) -> int:
    films = swapi_api.get_films_data(film_id)
    return len(films[0]["species"])


print(f"Q1:有多少不同種族的人出現在第六部: {get_how_many_species_in_film(6)}\n")

# Q2 請依據電影集數去排序電影名字


def sort_by_episode() -> list[dict]:
    films = swapi_api.get_films_data()
    sorted_films = sorted(films, key=lambda x: x["episode_id"])
    result = []
    for film in sorted_films:
        result.append({"episode_id": film["episode_id"], "title": film["title"]})
    return result


print(f"Q2:請依據電影集數去排序電影名字: {json.dumps(sort_by_episode(), indent=4)}\n")

# 請幫我挑出電影裡所有的車輛，馬力超過１０００的。


def get_vehicles_with_power_over_1000() -> list[dict]:
    vehicles = swapi_api.get_vehicles_data()
    result = []
    for vehicle in vehicles:
        try:
            if int(vehicle["max_atmosphering_speed"]) > 1000:
                result.append(
                    {
                        "name": vehicle["name"],
                        "max_speed": int(vehicle["max_atmosphering_speed"]),
                    }
                )
        except (
            ValueError
        ):  # handle the case when the max_atmosphering_speed is not a number or unknown
            pass
    return result


print(
    f"Q3:請幫我挑出電影裡所有的車輛，馬力超過１０００的。: {json.dumps(get_vehicles_with_power_over_1000(), indent=4)}"
)

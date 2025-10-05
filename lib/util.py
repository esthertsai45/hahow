import requests
from typing import Optional


class Paginator:
    """
    handle the pagination of the API
    """

    @staticmethod
    def fetch_all(url: str) -> list:
        all_results = []
        current_url: Optional[str] = url

        while current_url:
            try:
                response = requests.get(current_url)
                response.raise_for_status()
                data = response.json()

                if isinstance(data, dict):
                    if "results" in data:
                        all_results.extend(data["results"])
                        current_url = data.get("next")
                    else:
                        all_results.append(data)
                        current_url = None
                elif isinstance(data, list):
                    all_results.extend(data)
                    current_url = None
                else:
                    all_results.append(data)
                    current_url = None

            except requests.exceptions.RequestException as e:
                print(f"API request error: {e}")
                break
        return all_results

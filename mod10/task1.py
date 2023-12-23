import requests
import json


class SWAPIRequest:
    """
    Класс для выполнения запросов к Star Wars API.
    """
    @staticmethod
    def get_data(url: str) -> dict:
        """
        Получение данных из API по указанному URL.
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Failed to fetch data from {url}")

    @staticmethod
    def fetch_millennium_falcon_info() -> None:
        """
        Получение информации о пилотах легендарного корабля Millennium Falcon и сохранение в JSON-файле.
        """

        ship_info_url = 'https://swapi.dev/api/starships/10/'
        ship_info = SWAPIRequest.get_data(ship_info_url)

        pilots_info = []
        for pilot_url in ship_info.get('pilots', []):
            pilot = SWAPIRequest.get_data(pilot_url)
            pilot_info = {
                'name': pilot.get('name', ''),
                'height': pilot.get('height', ''),
                'weight': pilot.get('mass', ''),
                'homeworld': SWAPIRequest.get_data(pilot.get('homeworld', '')).get('name', ''),
                'homeworld_url': pilot.get('homeworld', ''),
            }
            pilots_info.append(pilot_info)

        result = {
            'ship_name': ship_info.get('name', ''),
            'starship_class': ship_info.get('starship_class', ''),
            'max_atmosphering_speed': ship_info.get('max_atmosphering_speed', ''),
            'pilots': pilots_info
        }

        with open('millennium_falcon.json', 'w') as file:
            json.dump(result, file, indent=4)

        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    try:
        sw = SWAPIRequest()
        sw.fetch_millennium_falcon_info()
    except (Exception, ValueError) as e:
        print(e)

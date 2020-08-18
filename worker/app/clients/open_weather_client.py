import requests

from app.core.config import settings
from app import exceptions


class OpenWeatherClient:

    def __init__(self, client=requests.Session(), settings=settings):
        self.client = client
        self.settings = settings

    def current_weather(self, city: dict) -> dict:
        try:
            url = f'{self.settings.OPEN_WEATHER_HOST}/data/2.5/weather?' \
                  f'q={city.get("name")},{city.get("state_code")},{city.get("country")}' \
                  f'&appid={settings.OPEN_WEATHER_KEY}'

            response = self.client.get(url, timeout=(self.settings.CONNECT_TIMEOUT, self.settings.READ_TIMEOUT))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as exc:

            if exc.response.status_code == 404:
                return {}

            raise exceptions.OpenWeatherClientException(
                f'An error occurred while processing your request, status code: {exc.response.status_code}'
            )


weather_client = OpenWeatherClient()

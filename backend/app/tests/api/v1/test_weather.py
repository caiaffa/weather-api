from fastapi.testclient import TestClient

from app.core.config import settings


def test_process_weather_by_city(client: TestClient) -> None:
    data = {
      "name": "blumenau",
      "state_code": "sc",
      "country_code": "br"
    }
    response = client.post(f"{settings.API_V1}/weather", json=data)
    assert response.status_code == 201
    content = response.json()
    assert content["msg"] == "success"


def test_get_weather_by_city(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1}/weather?name=blumenau&state_code=sc&country_code=br")
    assert response.status_code == 200
    content = response.json()
    assert content["msg"] == "success"


def test_get_weather_with_invalid_city(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1}/weather?name=aaaa&state_code=xxx&country_code=aaaa")
    assert response.status_code == 404

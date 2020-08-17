from fastapi.testclient import TestClient

from app.core.config import settings


def test_health_check(client: TestClient) -> None:
    data = {"msg": "ok"}
    response = client.get(f"{settings.API_V1}/health-check/")
    assert response.status_code == 200
    content = response.json()
    assert content["msg"] == data["msg"]

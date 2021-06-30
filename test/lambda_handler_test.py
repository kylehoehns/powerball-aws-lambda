from src.lambda_handler import LambdaHandler
from src.powerball_response import PowerballResponse


def test_handle_event(monkeypatch):

    handler = LambdaHandler()
    monkeypatch.setattr(handler, "powerball_service", MockPowerballService)

    response = handler.handle_event({}, {})
    assert response["statusCode"] == 200
    assert response["headers"]["Content-Type"] == "application/json"
    assert response["body"] == '{"numbers": [1, 2, 3, 4, 5, 6], "powerball": 7}'


class MockPowerballService:
    def generate_random_powerball():
        return PowerballResponse([1, 2, 3, 4, 5, 6], 7)

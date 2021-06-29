from src.powerball_response import PowerballResponse
from src.powerball_service import PowerballService


def test_generate_random_powerball():
    response = PowerballService().generate_random_powerball()
    assert type(response) is PowerballResponse
    assert len(set(response.numbers)) == 6
    for num in response.numbers:
        assert 1 <= num <= 70
    assert 1 <= response.powerball <= 26

from src.powerball_response import PowerballResponse


def test_create_powerball_response():
    numbers = [1, 2, 3]
    powerball = 7
    response = PowerballResponse(numbers, powerball)
    assert response.numbers == numbers
    assert response.powerball == powerball

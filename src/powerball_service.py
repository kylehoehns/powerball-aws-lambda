import random
from typing import List

from .powerball_response import PowerballResponse


class PowerballService:
    def generate_random_powerball(self) -> PowerballResponse:
        numbers = _build_random_list(1, 71)
        powerballs = _build_random_list(1, 26)
        return PowerballResponse(numbers[:6], powerballs[0])


def _build_random_list(start: int, end_exclusive: int) -> List[int]:
    random_list = list(range(start, end_exclusive))
    random.shuffle(random_list)
    return random_list

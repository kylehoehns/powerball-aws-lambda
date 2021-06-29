import random

from .powerball_response import PowerballResponse


class PowerballService:
    def generate_random_powerball(self) -> PowerballResponse:
        numbers = _buildRandomList(1, 71)
        powerballs = _buildRandomList(1, 26)
        return PowerballResponse(numbers[:6], powerballs[0])


def _buildRandomList(start, endExclusive):
    l = list(range(start, endExclusive))
    random.shuffle(l)
    return l
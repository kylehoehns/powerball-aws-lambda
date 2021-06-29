import json
from typing import Any

from .powerball_service import PowerballService


class LambdaHandler:
    def __init__(self) -> None:
        self.powerballService = PowerballService()

    def handleEvent(self, event, context) -> Any:
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                self.powerballService.generate_random_powerball(),
                default=lambda x: x.__dict__,
            ),
        }


def lambda_handler(event, context):
    return LambdaHandler().handleEvent(event, context)

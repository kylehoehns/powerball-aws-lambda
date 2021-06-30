import json
from typing import Any

from .powerball_service import PowerballService


class LambdaHandler:
    def __init__(self) -> None:
        self.powerball_service = PowerballService()

    def handle_event(self, event, context) -> Any:
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                self.powerball_service.generate_random_powerball(),
                default=lambda response: response.__dict__,
            ),
        }


def lambda_handler(event, context):
    return LambdaHandler().handle_event(event, context)

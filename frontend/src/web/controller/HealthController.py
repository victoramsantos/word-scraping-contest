import json

from flask import (
    Blueprint)

from src.web.controller import health_service

health_controller = Blueprint('HealthController', __name__)


class HealthController:
    @staticmethod
    @health_controller.route('/health', methods=['GET'])
    def health():
        is_health, response = health_service.health_checker()
        return json.dumps(response), 200 if is_health else 503, {'Content-Type': 'application/json'}

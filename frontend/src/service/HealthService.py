from src.repository.GraphRepository import GraphRepository


class HealthService:

    def __init__(self, repository: GraphRepository):
        self.__repository = repository

    def health_checker(self):
        database: bool = self.__repository.status()

        return database, {
          "backend_status": "ok" if database else "nok",
          "frontend_status": "ok"
        }

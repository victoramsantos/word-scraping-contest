import os

from src.repository.GraphRepository import GraphRepository
from src.repository.graphdatabase.Neo4jDatabase import Neo4jDatabase
from src.service.HealthService import HealthService
from src.service.WordService import WordService

graph_repository: GraphRepository = GraphRepository(
    database=Neo4jDatabase()
)

word_service: WordService = WordService(
    repository=graph_repository
)

health_service: HealthService = HealthService(
    repository=graph_repository
)

DEFAULT_WORD: str = os.getenv("DEFAULT_WORD")
APPLICATION_PATH: str = f"http://{os.getenv('FLASK_HOST')}:{os.getenv('FLASK_PORT')}?word="
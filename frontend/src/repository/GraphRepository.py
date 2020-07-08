from src.repository.graphdatabase.GraphDatabaseInterface import GraphDatabaseInterface


class GraphRepository:
    def __init__(self, database: GraphDatabaseInterface):
        self.__database: GraphDatabaseInterface = database

    def find_word(self, word: str) -> dict:
        return self.__database.get_all_relations_for(word)

    def status(self) -> bool:
        return self.__database.status()
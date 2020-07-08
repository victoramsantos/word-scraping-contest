import os

from neo4j import GraphDatabase

from src.library.logger.Logger import Logger
from src.repository.graphdatabase.GraphDatabaseInterface import GraphDatabaseInterface


class Neo4jDatabase(GraphDatabaseInterface):
    def __init__(self):
        self.__graphDB_Driver = GraphDatabase.driver(
            uri=os.getenv("NEO4J_URI"),
            auth=(
                os.getenv("NEO4J_USERNAME"),
                os.getenv("NEO4J_PASSWORD")
            )
        )
        self.__is_synonym = "IS_SYNONYM"
        self.__is_antonym = "IS_ANTONYM"

    def status(self) -> bool:
        try:
            with self.__graphDB_Driver.session() as graphDB_Session:
                graphDB_Session.run("Match () Return 1 Limit 1")
                return True
        except:
            return False

    def __insert_relation(self, word_a, word_b, relation):
        merge_a = "MERGE (" + word_a + ":Word {name:'" + word_a + "'}) "
        merge_b = "MERGE (" + word_b + ":Word {name:'" + word_b + "'}) "
        merge_relation = "MERGE (" + word_a + ")-[:" + relation + "]->(" + word_b + ") "

        Logger.debug("__insert_relation->merge_a", merge_a)
        Logger.debug("__insert_relation->merge_b", merge_b)
        Logger.debug("__insert_relation->merge_relation", merge_relation)

        with self.__graphDB_Driver.session() as graphDB_Session:
            graphDB_Session.run(merge_a + merge_b + merge_relation)

    def insert_synonym(self, word_a, word_b):
        self.__insert_relation(word_a, word_b, self.__is_synonym)

    def insert_antonym(self, word_a, word_b):
        self.__insert_relation(word_a, word_b, self.__is_antonym)

    def get_all_relations_for(self, word) -> dict:
        return {
            "word": word,
            "synonyms": self.__get_all_connections_by(word, self.__is_synonym),
            "antonyms": self.__get_all_connections_by(word, self.__is_antonym)
        }

    def __get_all_connections_by(self, word, relation):
        query = "MATCH (:Word { name: '" + word + "' })<-[:" + relation + "]->(connections:Word) " \
                                                                          "RETURN connections"

        Logger.debug("__get_all_connections_by->query", query)
        arr = []

        with self.__graphDB_Driver.session() as graphDB_Session:
            results = graphDB_Session.run(query)
            for node in results:
                arr.append(node[0].get("name"))

        Logger.debug("__get_all_connections_by->query->size", len(arr))
        return arr

import os

from neo4j import GraphDatabase

uri = os.getenv("NEO4J_URI")
userName = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

__is_synonym = "IS_SYNONYM"
__is_antonym = "IS_ANTONYM"

graphDB_Driver = GraphDatabase.driver(uri, auth=(userName, password))


def __insert_relation(word_a, word_b, relation):
    merge_a = "MERGE (" + word_a + ":Word {name:'" + word_a + "'}) "
    merge_b = "MERGE (" + word_b + ":Word {name:'" + word_b + "'}) "
    merge_relation = "MERGE (" + word_a + ")-[:" + relation + "]->(" + word_b + ") "

    print(merge_a)
    print(merge_b)
    print(merge_relation)

    with graphDB_Driver.session() as graphDB_Session:
        graphDB_Session.run(merge_a + merge_b + merge_relation)


def insert_synonym(word_a, word_b):
    __insert_relation(word_a, word_b, __is_synonym)


def insert_antonym(word_a, word_b):
    __insert_relation(word_a, word_b, __is_antonym)


def contains(word):
    elements = get_all_relations_for(word)
    return len(elements["synonyms"]) > 1


def get_all_relations_for(word) -> dict:
    return {
        "word": word,
        "synonyms": __get_all_connections_by(word, __is_synonym),
        "antonyms": __get_all_connections_by(word, __is_antonym)
    }


def __get_all_connections_by(word, relation):
    query = "MATCH (:Word { name: '" + word + "' })<-[:" + relation + "]->(connections:Word) " \
                                                                      "RETURN connections"

    arr = []

    with graphDB_Driver.session() as graphDB_Session:
        results = graphDB_Session.run(query)
        for node in results:
            arr.append(node[0].get("name"))

    return arr

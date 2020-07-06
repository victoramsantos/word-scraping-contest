from scraper.scraper import scraper_word
from database.database import insert_synonym, insert_antonym, get_all_relations_for
from unidecode import unidecode as remove_accents


def populate_database():
    word = "paixão"
    sanitized_word = remove_accents(word)
    synonyms, antonyms = scraper_word(word)
    print(synonyms)
    print(antonyms)

    for synonym in synonyms:
        # print(f"{word} is_synonym {synonym}")
        insert_synonym(sanitized_word, remove_accents(synonym))

    for antonym in antonyms:
        # print(f"{word} is_antonym {antonym}")
        insert_antonym(sanitized_word, remove_accents(antonym))


def query_database(word):
    return get_all_relations_for(word)


def from_domain_to_dto(domain):
    word = domain["word"]

    nodes = [{'data': {'id': word}}]
    nodes += [{
        "data": {
            "id": connection,
            "is": "synonym"
        }
    } for connection in domain["synonyms"]]

    nodes += [{
        "data": {
            "id": connection,
            "is": "antonym"
        }
    } for connection in domain["antonyms"]]

    print(nodes)

    edges = [{
        "data": {
            "id": f"{word}-{connection}",
            "source": word,
            "target": connection,
            "relation": "is_synonym_of"
        }
    } for connection in domain["synonyms"]]

    edges += [{
        "data": {
            "id": f"{word}-{connection}",
            "source": word,
            "target": connection,
            "relation": "is_antonym_of"
        }
    } for connection in domain["antonyms"]]

    print(edges)
    # elements: {
    #     nodes: [
    #         {data: {id: 'a'}},
    #         {data: {id: 'b'}}
    #     ],
    #     edges: [
    #         {data: {id: 'ab', source: 'a', target: 'b'}}
    #     ]
    # },


if __name__ == '__main__':
    from_domain_to_dto(query_database("amor"))

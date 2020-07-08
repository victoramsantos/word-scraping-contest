from src.repository.GraphRepository import GraphRepository


class WordService:
    def __init__(self, repository: GraphRepository):
        self.__repository = repository

    def word_analysis(self, word: str) -> str:
        domain_elements: dict = self.__repository.find_word(
            word=word
        )
        return self.__parse_domain_to_dto(domain_elements)

    def __parse_domain_to_dto(self, domain_elements: dict) -> str:
        _center = "mid"
        _class_clickable = "clickable"

        _elements = [{'data': {'id': _center, 'name': domain_elements["word"]}, 'classes': _center}]
        _elements += [{
            "data": {
                "id": connection,
                "is_related": "synonym"
            },
            'classes': _class_clickable
        } for connection in domain_elements["synonyms"]]

        _elements += [{
            "data": {
                "id": connection,
                "is_related": "antonym"
            },
            'classes': _class_clickable
        } for connection in domain_elements["antonyms"]]

        _elements += [{
            "data": {
                "source": _center,
                "target": connection,
                "relation": "synonym"
            }
        } for connection in domain_elements["synonyms"]]

        _elements += [{
            "data": {
                "source": _center,
                "target": connection,
                "relation": "antonym"
            }
        } for connection in domain_elements["antonyms"]]

        return _elements.__str__()
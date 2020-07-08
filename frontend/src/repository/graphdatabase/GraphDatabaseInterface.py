
class GraphDatabaseInterface:
    def status(self) -> bool:
        pass

    def insert_synonym(self, word_a, word_b):
        pass

    def insert_antonym(self, word_a, word_b):
        pass

    def get_all_relations_for(self, word) -> dict:
        pass

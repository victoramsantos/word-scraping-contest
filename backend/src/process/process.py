import os

from unidecode import unidecode as remove_accents

from src.database import database
from src.database.database import insert_synonym, insert_antonym
from src.scraper.scraper import scraper_word

configuration = {
    'count': 0,
    'max': int(os.getenv("DEPTH_INTERACTIONS", 10))
}


def populate_database(word):
    configuration["count"] += 1
    print(f"\n\nRunning interaction {configuration['count']}/{configuration['max']} with word: {word}")

    synonyms, antonyms = scraper_word(word)
    sanitized_word = remove_accents(word)

    print(f"{word} - synonyms: {synonyms}")
    print(f"{word} - antonyms: {antonyms}")

    for synonym in synonyms:
        insert_synonym(sanitized_word, remove_accents(synonym))

    for antonym in antonyms:
        insert_antonym(sanitized_word, remove_accents(antonym))

    __run(synonyms)
    __run(antonyms)


def __run(words: list):
    for word in words:
        if configuration["count"] >= configuration["max"]:
            return

        if not database.contains(remove_accents(word)):
            populate_database(word)
            # p = multiprocessing.Process(target=populate_database, args=(word,))
            # p.start()

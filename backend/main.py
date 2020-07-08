import os
import sys


def has_database_environment():
    return True if os.getenv("NEO4J_URI") \
                   and os.getenv("NEO4J_USERNAME") \
                   and os.getenv("NEO4J_PASSWORD") \
        else False


if __name__ == '__main__':
    if not has_database_environment():
        print("You must set the env variables: NEO4J_URI, NEO4J_USERNAME and NEO4J_PASSWORD")
        sys.exit(1)

    from src.process.process import populate_database

    word = os.getenv("FIRST_WORD", "amor")
    populate_database(word)

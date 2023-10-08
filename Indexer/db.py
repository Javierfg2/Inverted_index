import os
import sqlite3
import Indexer.utils


def create_inverted_index2(route):
    """
    -Function designed to generate an inverted index in a relational database shape

    :param route: route that contains the Datalake directory

    :return: void function
    """

    if os.path.exists("../Datamart/datamart.db"):
        return None

    db_connection = sqlite3.connect("../Datamart/datamart.db")
    cursor = db_connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inverted_index (
            word TEXT PRIMARY KEY,
            file_names TEXT
        )
    ''')

    for file_name in os.listdir(route):

        if file_name.endswith('.txt'):
            file = os.path.join(route, file_name)
            content = Indexer.utils.eliminate_metadata(file)
            content = Indexer.utils.normalizer(content)
            unique_words = set()

            for word in content.split():
                if len(word) > 2 and word not in unique_words:
                    unique_words.add(word)

                    cursor.execute("SELECT file_names FROM inverted_index WHERE word=?", (word,))
                    existing_files = cursor.fetchone()

                    if existing_files is not None:
                        existing_files = existing_files[0].split(", ")
                        existing_files.append(file_name)
                        new_files = ", ".join(existing_files)

                        cursor.execute("UPDATE inverted_index SET file_names=? WHERE word=?", (new_files, word))
                    else:
                        cursor.execute("INSERT INTO inverted_index (word, file_names) VALUES (?, ?)", (word, file_name))

    db_connection.commit()
    db_connection.close()


def find_books_for_word(word):
    """
    -Function designed to search for a specific word in the inverted index and return a list of occurrences

    :param word: the word that is going to be browsed

    :return: a structured list that contains the book files in which the searched word appears
    """

    db_connection = sqlite3.connect("../Datamart/datamart.db")
    cursor = db_connection.cursor()

    cursor.execute("SELECT file_names FROM inverted_index WHERE word=?", (word,))
    result = cursor.fetchone()

    if result is not None:
        return result[0].split(", ")
    else:
        print("Word not found")

    db_connection.close()

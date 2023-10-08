import os.path
import time
import unittest
import Indexer.db


class TestDb(unittest.TestCase):

    def test_find_books_for_word_exists(self):
        result = Indexer.db.find_books_for_word("hello")
        self.assertEqual(['Book4.txt'], result)

    def test_find_books_for_word_not_exists(self):
        result = Indexer.db.find_books_for_word("hoal")
        self.assertEqual(None, result)

    def test_create_inverted_index_2(self):
        if os.path.exists("../Datamart/datamart.db"):
            os.remove("../Datamart/datamart.db")

        Indexer.db.create_inverted_index2("C:/Users/pablo/Desktop/UNIVERSIDAD/TERCERO/BD/inverted_index_py/DataLake")

        if os.path.exists("../Datamart/datamart.db"):
            result = True

        self.assertEqual(True, result)

    def test_performance(self):
        if os.path.exists("../Datamart/datamart.db"):
            os.remove("../Datamart/datamart.db")

        i = time.time()

        Indexer.db.create_inverted_index2("C:/Users/pablo/Desktop/UNIVERSIDAD/TERCERO/BD/inverted_index_py/DataLake")
        Indexer.db.find_books_for_word("same")

        f = time.time()

        result = f -i

        print("Execution time = ", result)


if __name__ == '__main__':
    unittest.main()

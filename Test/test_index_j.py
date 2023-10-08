import unittest
import Indexer.index_j
import os
import time


class TestIndexJ(unittest.TestCase):

    def test_search_word_exists(self):

        if not os.path.exists("../Datamart/datamart.json"):
            datamart = {}
            Indexer.index_j.create_inverted_index("C:/Users/pablo/Desktop/UNIVERSIDAD/TERCERO/BD/inverted_index_py/DataLake" ,datamart)

        result = Indexer.index_j.search_word("hello")
        self.assertEqual(['Book4.txt'], result)

    def test_search_word_not_exist(self):

        if not os.path.exists("../Datamart/datamart.json"):
            datamart = {}
            Indexer.index_j.create_inverted_index("C:/Users/pablo/Desktop/UNIVERSIDAD/TERCERO/BD/inverted_index_py/DataLake" ,datamart)

        result = Indexer.index_j.search_word("hola")
        self.assertEqual(None, result)

    def test_create_inverted_index(self):
        if os.path.exists("../Datamart/datamart.json"):
            os.remove("../Datamart/datamart.json")

        datamart = {}
        Indexer.index_j.create_inverted_index("C:/Users/pablo/Desktop/UNIVERSIDAD/TERCERO/BD/inverted_index_py/DataLake", datamart)

        if os.path.exists("../Datamart/datamart.json"):
            result = True

        self.assertEqual(True, result)

    def test_performance(self):
        if os.path.exists("../Datamart/datamart.json"):
            os.remove("../Datamart/datamart.json")

        datamart = {}

        i = time.time()

        Indexer.index_j.create_inverted_index("C:/Users/pablo/Desktop/UNIVERSIDAD/TERCERO/BD/inverted_index_py/DataLake", datamart)
        Indexer.index_j.search_word("same")

        f = time.time()

        result = f -i

        print("Execution time = ", result)


if __name__ == '__main__':
    unittest.main()

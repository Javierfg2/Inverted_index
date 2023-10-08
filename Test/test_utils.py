import os
import unittest
import Indexer.utils


class TestUtils(unittest.TestCase):

    def test_normalizer_punctuation(self):
        result = Indexer.utils.normalizer("hello-its; me how are you")
        self.assertEqual(result, "hello its  me how are you")

    def test_normalizer_capital(self):
        result = Indexer.utils.normalizer("WORDS IN CAPITAL LETTERS SHOULD")
        self.assertEqual(result, "words in capital letters should")

    def test_normalizer_both(self):
        result = Indexer.utils.normalizer("This phrase sh;ould be normalize;")
        self.assertEqual(result, "this phrase sh ould be normalize ")

    def test_eliminate_metadata(self):
        with open("test.txt", 'w') as fl:
            fl.write("*** metadata ***\n")
            fl.write("content to be shown")
        result = Indexer.utils.eliminate_metadata('test.txt')
        os.remove("test.txt")
        self.assertEqual(result, "content to be shown")


if __name__ == '__main__':
    unittest.main()

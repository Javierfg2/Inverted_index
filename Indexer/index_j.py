import json
import os
from Indexer import utils


def create_inverted_index(route, datamart):
    """
    -Function designed to generate an inverted index as a json file, in case it does not exist already

    :param route: route that contains the Datalake directory

    :param datamart: empty datamart that will contain the inverted index

    :return: void function
    """

    if os.path.exists("../Datamart/datamart.json"):
        return None

    for file_name in os.listdir(route):

        if file_name.endswith('.txt'):
            file = os.path.join(route, file_name)
            content = utils.eliminate_metadata(file)
            content = utils.normalizer(content)

            for word in content.split():
                if len(word) > 2:
                    if word in datamart:
                        if file_name in datamart[word]:
                            pass
                        else:
                            datamart[word].append(file_name)
                    else:
                        datamart[word] = [file_name]

    with open("../Datamart/datamart.json", "w") as json_file:
        json.dump(datamart, json_file)

    return datamart


def search_word(word):
    """
    -Function designed to search for a specific word in the inverted index and return a list of occurrences

    :param word: the word that is going to be browsed

    :return: a structured list that contains the book files in which the searched word appears
    """

    try:
        with open("../Datamart/datamart.json", "r") as json_file:
            data = json.load(json_file)
            if word in data:
                return data[word]
            else:
                print("Word not found")

    except FileNotFoundError:
        print("Datamart not found")

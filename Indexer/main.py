import index_j
import db

datamart = {}
route = "C:/Users/pablo/Desktop/UNIVERSIDAD/TERCERO/BD/inverted_index_py/DataLake"

print("What search method would you like to use?")
print("JSON(1) or DB(2)")

try:
    election = int(input("Method: "))

    if election == 1:
        index_j.create_inverted_index(route, datamart)
        word = input("What word do you want to search: ")
        list = index_j.search_word(word)

        if list is not None:
            print("This word appears in: ", list)

    elif election == 2:
        db.create_inverted_index2(route)
        word = input("What word do you want to search: ")
        list = db.find_books_for_word(word)

        if list is not None:
            print("This word appears in: ", list)

    else:
        print("Invalid method")

except ValueError:
    print("Invalid method")

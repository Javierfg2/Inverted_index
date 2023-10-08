import re


def normalizer(book):
    """
    -Function designed to normalize a text converting it to lower cases and deleting any symbol that is not a letter
    under UTF-8 standar.

    :param book: a string variable containing a text

    :return book: the modified string normalized
    """

    book = book.lower()
    book = re.sub(r'[^a-zA-Z\s]', ' ', book)

    return book


def eliminate_metadata(input_file):
    """
    -Function designed to eliminate the metadata that appears at the beginning of the book files.

    :param input_file: file that needs to be processed to eliminate its metadata

    :return: string variable which stores the file´s content without metadata
    """

    try:
        with open(input_file, 'r', encoding='utf-8') as input_file:
            found_first_occurrence = False

            content_without_metadata = []

            lines = input_file.readlines()

            for line in lines:
                if '***' in line and not found_first_occurrence:
                    found_first_occurrence = True
                elif found_first_occurrence:
                    if '***' in line:
                        break

                    content_without_metadata.append(line)

        return ''.join(content_without_metadata)

    except Exception as e:
        print(f"Error: {e}")
        return None

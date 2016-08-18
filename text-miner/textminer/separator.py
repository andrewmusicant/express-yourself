import re


def words(text):
    words = re.findall(r"[\w]*[-]*[A-Za-z]+", text)
    if words == []:
        return None
    return words


# def phone_number(text):
#     return re.findall(r"((?:\(?(\d{3})\)?)[\-\.]?\s*)?((\d{3})[\-\.]?\s*(\d{4}))",
#                     text)

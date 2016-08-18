import re


def binary(given_str):
    return re.match(r"^[0|1]+$", given_str)


def binary_even(given_str):
    return re.match(r".+0$", given_str)


def hex(given_str):
    return re.match(r"^[A-F0-9]+$", given_str)


def word(given_str):
    return re.match(r"^[\w]*[-]*[A-Za-z]+$", given_str)


def words(given_str, count=None):
    words = re.findall(r"[\w]*[-]*[A-Za-z]+", given_str)
    if count is None:
        return len(words) == len(given_str.split(' '))
    else:
        return len(words) == count


def phone_number(given_str):
    return re.match(r"(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?\s*(\d{4})",
                    given_str)


# def money(given_str):
#     return re.match(r"^(?:\$)[0-9]+?[\,]?([\d]{1-3})[\.]?([0-9]{2})?$",
#                     given_str)

def zipcode(given_str):
    return re.match(r"^\d{5}(?:[-\s]\d{4})?$", given_str)


def date(given_str):
    return re.match(r"(\d+[\/|\-]\d+[\/|\-]\d+)", given_str)

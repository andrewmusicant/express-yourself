import re


def phone_numbers(text):
    list_of_nums = re.findall(r"\(\d{3}\)[\s][\d]{3}[-][\d]{4}", text)
    return list_of_nums

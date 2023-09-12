def raise_register(word):
    """увеличивает регистр всех букв"""
    return word.upper()


def raise_first_letter(string_):
    """увеличивает регистр первой буквы каждого слова"""
    string_list = string_.split()
    result_string = ' '.join(string_list).title()

    return result_string

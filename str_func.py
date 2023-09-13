def raise_register(text_):
    """увеличивает регистр каждой буквы"""
    return text_.upper()


def raise_first_letter(string_):
    """увеличивает регистр первой буквы каждого слова"""
    string_list = string_.split()
    result_string = ' '.join(string_list).title()

    return result_string

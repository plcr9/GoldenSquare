def extract_uppercase(mixed_words):
    new_list = mixed_words.split()
    result = [word for word in new_list if word.isupper()]
    return result


import string

def extract_uppercase(mixed_words):
    new_list = mixed_words.split()
    new_list2 = [''.join(char for char in item if char not in string.punctuation) for item in new_list]
    result = [word for word in new_list2 if word.isupper()]
    return result

def extract_no_value(no_words):
    if no_words is None:
        raise Exception("Value cannot be None")


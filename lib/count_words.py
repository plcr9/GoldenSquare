def count_words(string):
    if string == " ":
        return 0
    else:
        return len(string.strip().split(" "))


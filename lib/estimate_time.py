def estimate_reading_time(text):
    if text == "":
        raise Exception("Cannot estimate reading time for empty text.")
    words = text.split()
    word_count = len(words)
    return word_count / 200
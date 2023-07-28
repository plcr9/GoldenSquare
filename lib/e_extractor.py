def e_extractor(str):
    if "e" in str:
        letter_es = [letter for letter in str if letter == "e"]
        non_letter_es = [letter for letter in str if letter != "e"]
        letters = letter_es + non_letter_es
        return "".join(letters)

    else:
        return str
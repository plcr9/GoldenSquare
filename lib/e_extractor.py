def e_extractor(str):
    if "e" in str:
        new_str = ""
        for letter in str:
            if letter == "e":
                new_str = "e" + new_str
            else:
                new_str = new_str + letter
        return new_str
    else:
        return str
def is_pangram(sentence):
    letters_set = set()
    for letter in sentence.lower():
        if letter.isalpha() and not letter.isspace():
            letters_set.add(letter)
    if len(letters_set) == 26:
        return True
    return False

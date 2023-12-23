def is_isogram(string):
    letters_set = set()
    string = string.replace("-", "")
    string = string.replace(" ", "")
    for letter in string.lower():
        if letter.isalpha():
            letters_set.add(letter)
    if len(letters_set) == len(string):
        return True
    return False

def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_string = ""
    for letter in text:
        position = alphabet.find(letter.lower())
        if position + 1 + key < len(alphabet):
            new_letter = alphabet[position + key]
        elif position + 1 + key >= len(alphabet):
            new_letter = alphabet[position + key - len(alphabet)]
        if letter.islower():
            encoded_string += new_letter
        elif letter.isupper():
            encoded_string += new_letter.upper()
        elif letter.isspace():
            encoded_string += " "
        else:
            encoded_string += letter
    return encoded_string

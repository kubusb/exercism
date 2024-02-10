ALPHABET="ABCDEFGHIJKLMNOPQRSTUVXYZ"
def rows(letter):
    letter_position = ALPHABET.find(letter)
    result = []
    external_spaces = 0
    internal_spaces = letter_position + 1
    if letter == "A":
        result.append("A")
    else:
        while internal_spaces > 0:
            print("{}{}{}{}{}".format(external_spaces, ALPHABET[letter_position], internal_spaces, ALPHABET[letter_position], external_spaces))
            external_spaces += 1
            internal_spaces -= 2
            letter_position -= 1
    return result
#-A-
#B--B
#-A-
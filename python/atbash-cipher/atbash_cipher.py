""" Atbash cipher """
PLAIN =  "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    """ Encodes plain text as described"""
    coded_result_without_spaces = ""
    for letter in plain_text.casefold():
        position = PLAIN.find(letter)
        if letter.isdigit():
            coded_result_without_spaces += letter
        if letter.isspace() or position == -1:
            continue
        position = PLAIN.find(letter)
        coded_result_without_spaces += CIPHER[position]

    def format_coded_result(coded_result_without_spaces):
        chunks = [coded_result_without_spaces[i:i+5] for i in range(0, len(coded_result_without_spaces), 5)]
        coded_result_with_spaces = ' '.join(chunks)
        return coded_result_with_spaces

    return format_coded_result(coded_result_without_spaces)

def decode(ciphered_text):
    """ Decodes ciphered text into plain text without spaces"""
    decoded_result = ""
    for letter in ciphered_text.casefold():
        position = CIPHER.find(letter)
        if letter.isdigit():
            decoded_result += letter
        if letter.isspace() or position == -1:
            continue
        position = CIPHER.find(letter)
        decoded_result += PLAIN[position]
    return decoded_result

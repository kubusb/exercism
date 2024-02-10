ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def rows(letter):
    letter_position = ALPHABET.find(letter)
    result = []
    current_row = letter_position
    external_spaces = 0
    if current_row == 0:
        result.append("A")
    else:
        while current_row >= 0:
            internal_spaces = 2 * current_row - 1
            current_letter = ALPHABET[current_row]
            external_spaces_string = external_spaces * " "
            internal_spaces_string = internal_spaces * " "
            current_line = ""
            if current_row == letter_position:
                current_line = current_letter + internal_spaces_string + current_letter
                result.append(current_line)
            elif current_row == 0:
                current_line = external_spaces_string + current_letter + external_spaces_string
                result.append(current_line)
                result.insert(0, current_line)
            else:
                current_line = external_spaces_string + current_letter + internal_spaces_string + current_letter + external_spaces_string
                result.append(current_line)
                result.insert(0, current_line)
            current_row -= 1
            external_spaces += 1
    return result

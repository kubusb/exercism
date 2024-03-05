def decode(string):
    if string == "":
        return ""

def encode(string):
    if string == "":
        return ""
    
    current_position = 0
    result = ""
    while current_position <= len(string):
        if string[current_position:current_position+1] != string[current_position+1:current_position+2]:
            result += string[current_position:current_position+1]
            current_position += 1
        else:
            break
    return result
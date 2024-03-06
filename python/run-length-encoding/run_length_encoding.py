def decode(string):
    if string == "":
        return ""

def encode(input_str):
    if not input_str:
        return ""
    
    count = 1
    result = ""
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i-1]:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += input_str[i-1]
            count = 1
    if count > 1:
        result += str(count)
    result += input_str[-1]
    return result
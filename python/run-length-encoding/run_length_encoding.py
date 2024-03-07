def decode(encoded_str):
    decoded_str = ""
    i = 0
    while i < len(encoded_str):
        count_str = ''
        while encoded_str[i].isdigit():
            count_str += encoded_str[i]
            i += 1
        count = int(count_str) if count_str else 1
        decoded_str += encoded_str[i] * count
        i += 1
    return decoded_str

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
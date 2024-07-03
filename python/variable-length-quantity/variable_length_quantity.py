def encode(numbers):
    result = []
    for number in numbers:
        if number == 0:
            result.append(0)
        else:
            bytes_list = []
            while number > 0:
                byte = number & 0x7F
                number >>= 7
                if bytes_list:
                    byte |= 0x80
                bytes_list.insert(0, byte)
            result.extend(bytes_list)
    return result

def decode(bytes_):
    result = []
    current = 0
    for i, byte in enumerate(bytes_):
        if byte & 0x80:
            current = (current << 7) | (byte & 0x7F)
            if i == len(bytes_) - 1:
                raise ValueError("incomplete sequence")
        else:
            current = (current << 7) | byte
            result.append(current)
            current = 0
    
    return result
    
    if current != 0:
        raise ValueError("incomplete sequence")
    
    return result

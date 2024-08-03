def encode(plain_text, a, b):
    if not are_coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    
    result = ""
    for char in plain_text.lower():
        if char.isalpha():
            i = ord(char) - ord('a')
            encoded = (a * i + b) % 26
            result += chr(encoded + ord('a'))
        elif char.isdigit():
            result += char
    
    # Group the result into chunks of 5
    return ' '.join([result[i:i+5] for i in range(0, len(result), 5)])

def decode(ciphered_text, a, b):
    if not are_coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    
    a_inv = mod_inverse(a, 26)
    result = ""
    for char in ciphered_text.lower():
        if char.isalpha():
            y = ord(char) - ord('a')
            decoded = (a_inv * (y - b)) % 26
            result += chr(decoded + ord('a'))
        elif char.isdigit():
            result += char
    
    return result

def are_coprime(a, m):
    return gcd(a, m) == 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

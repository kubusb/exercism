import math
import re

def cipher_text(plain_text):
    # Step 1: Normalize the input
    normalized_text = re.sub(r'[^a-zA-Z0-9]', '', plain_text).lower()
    
    # Handle the case of empty normalized text
    if not normalized_text:
        return ""
    
    # Step 2: Determine the rectangle dimensions
    length = len(normalized_text)
    c = math.ceil(math.sqrt(length))
    r = math.ceil(length / c)
    
    # Step 3: Form the rectangle
    rectangle = [normalized_text[i:i + c] for i in range(0, length, c)]
    
    # Step 4: Read down the columns
    encoded_chunks = [''.join(row[i] if i < len(row) else ' ' for row in rectangle) for i in range(c)]
    
    # Step 5: Format the output
    encoded_text = ' '.join(encoded_chunks)
    
    return encoded_text

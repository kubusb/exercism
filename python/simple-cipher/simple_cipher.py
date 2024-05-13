import random
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))
        elif all(char in string.ascii_lowercase for char in key):
            self.key = key
        else:
            raise ValueError("Key must only contain lowercase letters.")
    
    def encode(self, text):
        return ''.join(
            chr(((ord(char) - ord('a') + ord(self.key[i % len(self.key)]) - ord('a')) % 26) + ord('a'))
            for i, char in enumerate(text)
        )

    def decode(self, text):
        return ''.join(
            chr(((ord(char) - ord('a') - (ord(self.key[i % len(self.key)]) - ord('a'))) % 26) + ord('a'))
            for i, char in enumerate(text)
        )

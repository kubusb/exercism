import re

def abbreviate(words):
    result = ""
    for word in re.split('-|_| ', words):
        if len(word) > 0:
            result += word[0]
    return result.upper()

def score(word, double_letter=None, triple_letter=None, double_word=None, triple_word=None):
    letter_values = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    
    score = 0
    for i, letter in enumerate(word.upper()):
        if double_letter and i in double_letter:
            score += letter_values.get(letter, 0) * 2
        elif triple_letter and i in triple_letter:
            score += letter_values.get(letter, 0) * 3
        else:
            score += letter_values.get(letter, 0)
    
    if double_word:
        score *= 2
    elif triple_word:
        score *= 3
    
    return score

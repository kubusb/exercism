import re

def count_words(subtitle):
    # Clean the subtitle text: Split into words based on any non-alphanumeric character (excluding apostrophes), and convert to lowercase
    cleaned_text = re.split(r"[^a-zA-Z0-9']+", subtitle.lower())
    
    # Remove single quotes from words
    cleaned_text = [word.strip("'") for word in cleaned_text if word.strip("'") != '']
    
    # Count the occurrences of each word
    word_counts = {}
    for word in cleaned_text:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

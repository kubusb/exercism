def find_anagrams(word, candidates):
    anagrams = []
    word_set = set(word)
    for candidate in candidates:
        if str(candidate).lower() != str(word).lower():
            if set(candidate).issubset(word_set):
                anagrams.append(candidate)
    return anagrams

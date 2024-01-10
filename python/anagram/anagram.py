def find_anagrams(word, candidates):
    # Function to normalize words (lowercase and sorted)
    def normalize(word):
        return ''.join(sorted(word.lower()))

    # Normalize the target word
    normalized_target = normalize(word)

    # Prepare the anagram set
    anagram_set = []

    # Check each candidate
    for candidate in candidates:
        if candidate.lower() != word.lower() and normalize(candidate) == normalized_target:
            anagram_set.append(candidate)

    return anagram_set

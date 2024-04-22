def recite(start, take=1):
    num_to_word = {
        0: "no", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"
    }
    
    verses = []
    for i in range(start, start - take, -1):
        current = num_to_word[i]
        next_one = num_to_word[i-1] if i > 1 else "no"

        current_bottles = "bottles" if i > 1 else "bottle"
        next_bottles = "bottles" if i > 2 else ("bottle" if i == 2 else "bottles")
        
        verse_lines = [
            f"{current.capitalize()} green {current_bottles} hanging on the wall,",
            f"{current.capitalize()} green {current_bottles} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {next_one} green {next_bottles} hanging on the wall."
        ]
        
        verses.extend(verse_lines)
        if i > 1 and i != start - take + 1:
            verses.append("")  # Adding a blank line between verses

    return verses

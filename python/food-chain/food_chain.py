def recite(start_verse, end_verse):
    animals = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse']
    reactions = {
        'spider': "It wriggled and jiggled and tickled inside her.",
        'bird': "How absurd to swallow a bird!",
        'cat': "Imagine that, to swallow a cat!",
        'dog': "What a hog, to swallow a dog!",
        'goat': "Just opened her throat and swallowed a goat!",
        'cow': "I don't know how she swallowed a cow!",
        'horse': "She's dead, of course!"
    }
    
    lyrics = []
    
    for i in range(start_verse - 1, end_verse):
        animal = animals[i]
        verse = [f"I know an old lady who swallowed a {animal}."]
        
        if animal == 'horse':
            verse.append(reactions[animal])
            lyrics.extend(verse)
            break
        
        if animal in reactions:
            verse.append(reactions[animal])
        
        for j in range(i, 0, -1):
            prev_animal = animals[j-1]
            current_animal = animals[j]
            if current_animal == 'bird' and prev_animal == 'spider':
                verse.append(f"She swallowed the {current_animal} to catch the {prev_animal} that wriggled and jiggled and tickled inside her.")
            else:
                verse.append(f"She swallowed the {current_animal} to catch the {prev_animal}.")
        
        verse.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        
        lyrics.extend(verse)
        
        if i < end_verse - 1:
            lyrics.append("")  # Add an empty line between verses
    
    return lyrics

def recite(start_verse, end_verse):
    rhyme_start = 'This is'
    verses = [ ' the horse and the hound and the horn that belonged to',
               ' the farmer sowing his corn that kept',
               ' the rooster that crowed in the morn that woke',
               ' the priest all shaven and shorn that married',
               ' the man all tattered and torn that kissed',
               ' the maiden all forlorn that milked',
               ' the cow with the crumpled horn that tossed',
               ' the dog that worried',
               ' the cat that killed',
               ' the rat that ate',
               ' the malt that lay in',
               ' the house']
    rhyme_end = ' that Jack built.'
    rhyme = [(rhyme_start + "".join(verses[12-i:12]) + rhyme_end) for i in range(start_verse,end_verse+1)]
    return rhyme

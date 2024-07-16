# Game status categories
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'

class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed_chars = set()
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        
        char = char.lower()
        if char in self.guessed_chars:
            self.remaining_guesses -= 1
        else:
            self.guessed_chars.add(char)
            if char not in self.word:
                self.remaining_guesses -= 1
        
        self.update_status()
        return self.get_status()

    def get_masked_word(self):
        return ''.join(char if char in self.guessed_chars else '_' for char in self.word)

    def get_status(self):
        return self.status

    def update_status(self):
        if all(char in self.guessed_chars for char in self.word):
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        else:
            self.status = STATUS_ONGOING
class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_frame = 1

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins")

        if self.is_game_over():
            raise ValueError("Cannot roll after game is over")

        if self.current_frame < 10:
            if len(self.rolls) % 2 == 1 and self.rolls[-1] + pins > 10:
                raise ValueError("Two rolls in a frame cannot score more than 10 points")

        if self.current_frame == 10:
            if len(self.rolls) == 20 and self.rolls[18] == 10 and self.rolls[19] < 10 and pins == 10:
                raise ValueError("Second bonus roll cannot be a strike if first one is not")
            if len(self.rolls) == 20 and self.rolls[18] + self.rolls[19] == 10 and pins > 10:
                raise ValueError("Bonus roll cannot score more than 10 points")

        self.rolls.append(pins)

        if self.current_frame < 10:
            if self._is_strike(len(self.rolls) - 1) or len(self.rolls) % 2 == 0:
                self.current_frame += 1
        elif self.current_frame == 10:
            if len(self.rolls) == 20 and not self._is_strike(18) and not self._is_spare(18):
                self.current_frame += 1
            elif len(self.rolls) == 21 and (self._is_strike(18) or self._is_spare(18)):
                self.current_frame += 1
            elif len(self.rolls) == 22:
                self.current_frame += 1

    def score(self):
        if not self.is_game_complete():
            raise ValueError("Game is not complete, cannot be scored")

        score = 0
        roll_index = 0

        for _ in range(10):
            if self._is_strike(roll_index):
                score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2

        return score

    def _is_strike(self, roll_index):
        return roll_index < len(self.rolls) and self.rolls[roll_index] == 10

    def _is_spare(self, roll_index):
        return roll_index + 1 < len(self.rolls) and self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def _strike_bonus(self, roll_index):
        return sum(self.rolls[roll_index + 1 : roll_index + 3])

    def _spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]

    def is_game_over(self):
        return self.current_frame > 10

    def is_game_complete(self):
        if len(self.rolls) < 20:
            return False
        if len(self.rolls) == 20 and not self._is_strike(18) and not self._is_spare(18):
            return True
        if len(self.rolls) == 21 and not self._is_strike(18):
            return True
        if len(self.rolls) == 22:
            return True
        return False
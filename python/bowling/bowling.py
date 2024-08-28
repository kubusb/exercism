class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_frame = 1
        self.current_frame_score = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins")

        if self.is_game_over():
            raise ValueError("Cannot roll after game is over")

        if self.current_frame < 10:
            if self.current_frame_score + pins > 10:
                raise ValueError("Two rolls in a frame cannot score more than 10 points")

        self.rolls.append(pins)

        if self.current_frame < 10:
            if pins == 10:  # Strike
                self.current_frame += 1
                self.current_frame_score = 0
            else:
                self.current_frame_score += pins
                if len(self.rolls) % 2 == 0:  # End of frame
                    self.current_frame += 1
                    self.current_frame_score = 0
        elif self.current_frame == 10:
            if len(self.rolls) == 20:
                if self.rolls[18] == 10:  # Strike in 10th frame
                    self.current_frame_score = 0
                else:
                    self.current_frame_score = self.rolls[18]
            elif len(self.rolls) == 21:
                if self.rolls[18] == 10:  # Strike in 10th frame
                    self.current_frame_score = self.rolls[19]
                elif self.rolls[18] + self.rolls[19] == 10:  # Spare in 10th frame
                    self.current_frame_score = 0
                else:
                    self.current_frame += 1
            elif len(self.rolls) == 22:
                self.current_frame += 1

    def score(self):
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
                score += sum(self.rolls[roll_index:roll_index+2])
                roll_index += 2

        return score

    def _is_strike(self, roll_index):
        return roll_index < len(self.rolls) and self.rolls[roll_index] == 10

    def _is_spare(self, roll_index):
        return roll_index + 1 < len(self.rolls) and sum(self.rolls[roll_index:roll_index+2]) == 10

    def _strike_bonus(self, roll_index):
        bonus = sum(self.rolls[roll_index+1:roll_index+3])
        return bonus if roll_index + 2 < len(self.rolls) else 0

    def _spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2] if roll_index + 2 < len(self.rolls) else 0

    def is_game_over(self):
        if len(self.rolls) < 20:
            return False
        if len(self.rolls) == 20 and self.rolls[18] + self.rolls[19] < 10:
            return True
        if len(self.rolls) == 21 and self.rolls[18] != 10:
            return True
        if len(self.rolls) == 22:
            return True
        return False
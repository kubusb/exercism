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

        else:  # 10th frame
            self._handle_10th_frame(pins)

    def _handle_10th_frame(self, pins):
        if len(self.rolls) == 19:
            return
        if len(self.rolls) == 20:
            if self.rolls[18] == 10 or self.rolls[18] + self.rolls[19] == 10:
                # Awaiting bonus roll(s) for a strike/spare in 10th frame
                return
        if len(self.rolls) >= 21:
            # Bonus roll logic
            if self.rolls[18] == 10:  # Strike in 10th frame
                if self.rolls[19] < 10 and pins == 10:
                    raise ValueError("The second bonus roll after a strike in the last frame cannot be a strike if the first one is not a strike")
                if len(self.rolls) == 22:
                    if self.rolls[20] + self.rolls[21] > 10:
                        raise ValueError("Two bonus rolls after a strike in the 10th frame cannot score more than 10 unless the first one is a strike")
            self.current_frame += 1

    def score(self):
        if self._is_incomplete_game():
            raise Exception("Cannot score an incomplete game")

        # Additional check for incomplete game with strike in 10th frame
        if len(self.rolls) == 19 and self.rolls[18] == 10:
            raise Exception("Cannot score an incomplete game")

        # New exception for incomplete bonus rolls after a strike in the last frame
        if len(self.rolls) == 20 and self.rolls[18] == 10:
            raise Exception("Cannot score before rolling the second bonus ball for a strike in the last frame")

        # New check for two bonus rolls after a strike in the last frame scoring more than 10 points
        if len(self.rolls) >= 20 and self.rolls[18] == 10:
            if len(self.rolls) == 21 and self.rolls[19] < 10 and self.rolls[20] > 10 - self.rolls[19]:
                raise Exception("Two bonus rolls after a strike in the last frame cannot score more than 10 points")
            elif len(self.rolls) == 22 and self.rolls[19] + self.rolls[20] > 10 and self.rolls[19] != 10:
                raise Exception("Two bonus rolls after a strike in the last frame cannot score more than 10 points")

        score = 0
        roll_index = 0

        for frame in range(10):
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

    def _is_incomplete_game(self):
        # Adjust incomplete game logic to account for 10th frame bonuses
        if len(self.rolls) < 12:
            return True
        if len(self.rolls) < 20:
            return False
        if self.rolls[18] == 10:
            return len(self.rolls) < 21 or len(self.rolls) == 22
        if self.rolls[18] + self.rolls[19] == 10:
            return len(self.rolls) < 21
        return len(self.rolls) < 20

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
        if len(self.rolls) == 21 and self.rolls[18] == 10 and self.rolls[19] != 10:
            return True
        if len(self.rolls) == 22:
            return True
        return False
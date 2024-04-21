class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        """Return the most recently added score."""
        return self.scores[-1]

    def personal_best(self):
        """Return the highest score from the list."""
        return max(self.scores)

    def personal_top_three(self):
        """Return the top three highest scores sorted from highest to lowest."""
        return sorted(self.scores, reverse=True)[:3]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.height = len(puzzle)
        self.width = len(puzzle[0]) if self.height > 0 else 0

    def search(self, word):
        for y in range(self.height):
            for x in range(self.width):
                result = self._search_from_point(word, x, y)
                if result:
                    return result
        return None

    def _search_from_point(self, word, x, y):
        directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, 1),   # down-right
            (-1, -1), # up-left
            (1, -1),  # down-left
            (-1, 1)   # up-right
        ]

        for dx, dy in directions:
            if self._check_direction(word, x, y, dx, dy):
                end_x = x + dx * (len(word) - 1)
                end_y = y + dy * (len(word) - 1)
                return (Point(x, y), Point(end_x, end_y))
        
        return None

    def _check_direction(self, word, x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < self.width and 0 <= ny < self.height):
                return False
            if self.puzzle[ny][nx] != word[i]:
                return False
        return True
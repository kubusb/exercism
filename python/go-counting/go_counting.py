WHITE = "W"
BLACK = "B"
NONE = ""

class Board:
    def __init__(self, board):
        self.board = board
        self.height = len(board)
        self.width = len(board[0]) if self.height > 0 else 0

    def territory(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError("Invalid coordinate")

        if self.board[y][x] != " ":
            return "", set()

        visited = set()
        territory = set()
        owner = set()

        def dfs(x, y):
            if not (0 <= x < self.width and 0 <= y < self.height):
                return
            if (x, y) in visited:
                return
            visited.add((x, y))

            current = self.board[y][x]
            if current == " ":
                territory.add((x, y))
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(x + dx, y + dy)
            elif current in "BW":
                owner.add(current)

        dfs(x, y)

        if len(owner) == 1:
            return list(owner)[0], territory
        return "", territory

    def territories(self):
        result = {"W": set(), "B": set(), "": set()}
        visited = set()

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in visited or self.board[y][x] != " ":
                    continue
                owner, territory = self.territory(x, y)
                result[owner].update(territory)
                visited.update(territory)

        return result

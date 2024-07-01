class ConnectGame:
    def __init__(self, board):
        self.board = [row.split() for row in board.strip().split('\n')]
        self.height = len(self.board)
        self.width = max(len(row) for row in self.board)

    def get_winner(self):
        if self.height == 1 and self.width == 1:
            return self.board[0][0] if self.board[0][0] in 'XO' else ''

        if self._check_win('O', self._top_edge(), self._bottom_edge()):
            return 'O'
        
        if self._check_win('X', self._left_edge(), self._right_edge()):
            return 'X'
        
        return ''

    def _check_win(self, player, start_edge, end_edge):
        visited = set()
        stack = list(start_edge)
        
        while stack:
            row, col = stack.pop()
            if (row, col) in end_edge and self._is_valid_move(row, col, player):
                return True
            
            if (row, col) not in visited and self._is_valid_move(row, col, player):
                visited.add((row, col))
                stack.extend(self._get_neighbors(row, col))
        
        return False

    def _is_valid_move(self, row, col, player):
        return 0 <= row < self.height and 0 <= col < len(self.board[row]) and self.board[row][col] == player

    def _get_neighbors(self, row, col):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
        return [(row + dr, col + dc) for dr, dc in directions if self._is_valid_move(row + dr, col + dc, self.board[row][col])]

    def _top_edge(self):
        return [(0, col) for col in range(len(self.board[0]))]

    def _bottom_edge(self):
        return [(self.height - 1, col) for col in range(len(self.board[-1]))]

    def _left_edge(self):
        return [(row, 0) for row in range(self.height)]

    def _right_edge(self):
        return [(row, len(self.board[row]) - 1) for row in range(self.height)]

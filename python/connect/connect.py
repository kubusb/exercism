class ConnectGame:
    def __init__(self, board):
        self.board = self.parse_board(board)
        print("Parsed board:")
        for row in self.board:
            print(" ".join(row))
        
    def parse_board(self, board_str):
        lines = board_str.strip().split('\n')
        board = [list(line.strip()) for line in lines]
        return board
    
    def in_bounds(self, x, y):
        return 0 <= x < len(self.board) and 0 <= y < len(self.board[x])
    
    def dfs(self, player, x, y, visited, target):
        if target(x, y):
            print(f"Player {player} has reached the target at ({x}, {y})")
            return True
        visited.add((x, y))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]  # Hexagonal directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny) and self.board[nx][ny] == player and (nx, ny) not in visited:
                if self.dfs(player, nx, ny, visited, target):
                    return True
        return False
    
    def has_won(self, player):
        visited = set()
        if player == 'O':
            target = lambda x, y: x == len(self.board) - 1
            starts = [(0, y) for y in range(len(self.board[0])) if self.board[0][y] == 'O']
        else:  # player == 'X'
            target = lambda x, y: y == len(self.board[0]) - 1
            starts = [(x, 0) for x in range(len(self.board)) if self.board[x][0] == 'X']
        
        for x, y in starts:
            print(f"Starting DFS for player {player} from ({x}, {y})")
            if self.dfs(player, x, y, visited, target):
                return True
        return False
    
    def get_winner(self):
        if self.has_won('O'):
            return "O"
        elif self.has_won('X'):
            return "X"
        else:
            return ""

# Debugging output for internal state verification
def debug_test():
    board_str = """
. O . .
O X X X
O O O .
X X O X
. O X .
"""
    game = ConnectGame(board_str)
    winner = game.get_winner()
    print(f"Winner: {winner}")

# Run the debug test
if __name__ == "__main__":
    debug_test()

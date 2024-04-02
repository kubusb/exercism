class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        
        if row < 0:
        # if the row parameter is negative
            raise ValueError("row not positive")

        if row > 7:
        # if the row parameter is not on the defined board
            raise ValueError("row not on board")

        if column < 0:
        # if the column parameter is negative
            raise ValueError("column not positive")

        if column > 7:
        # if the column parameter is not on the defined board
            raise ValueError("column not on board")

    def can_attack(self, another_queen):
        if self.column == another_queen.column and self.row == another_queen.row:
        # if both the queens are on the same location
            raise ValueError("Invalid queen position: both queens in the same square")
        # Check if the queens are in the same row, column, or diagonal
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False

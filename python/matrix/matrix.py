class Matrix:
    def __init__(self, matrix_string):
        # Convert the matrix string into a list of lists (2D list)
        self.matrix = [
            [int(num) for num in line.split()]
            for line in matrix_string.strip().split('\n')
        ]

    def row(self, index):
        # Return the row at the specified index (1-based index)
        return self.matrix[index - 1]

    def column(self, index):
        # Return the column at the specified index (1-based index)
        return [row[index - 1] for row in self.matrix]

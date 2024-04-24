NORTH, EAST, SOUTH, WEST = (0, 1), (1, 0), (0, -1), (-1, 0)

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x = x_pos
        self.y = y_pos
        self.directions = [NORTH, EAST, SOUTH, WEST]

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'R':
                self.direction = self.directions[(self.directions.index(self.direction) + 1) % 4]
            elif instruction == 'L':
                self.direction = self.directions[(self.directions.index(self.direction) - 1) % 4]
            elif instruction == 'A':
                self.x += self.direction[0]
                self.y += self.direction[1]

    @property
    def coordinates(self):
        return (self.x, self.y)

    @property
    def bearing(self):
        return self.direction

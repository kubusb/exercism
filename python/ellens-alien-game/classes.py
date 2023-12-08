"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    health = 3

    def __init__(self, coordinates):
        self.x_coordinate = coordinates[0]
        self.y_coordinate = coordinates[1]

    def hit(self):
        Alien.health -= 1

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def collision_detection(self):
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

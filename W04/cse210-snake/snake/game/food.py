import random
from game import constants
from game.actor import Actor
from game.point import Point
#TODO: Define food class here

class Food(Actor):

    def __init__(self):
        self._position = Point(30,10)
        self._points = 0
        self.set_text('@')

    def get_position(self):
        """Produces a random food location to be returned and compared with current head (_segment[0])
        position.

        Args:
            self(Food): instance of Food
        
        """
        return self._position

    def get_points(self):
        """Produces a random amount of points ranging from 1 to 5 and returns the value
        to be added to the total score

        Args:
            self(Food): instance of food
        
        """
        self._points = random.randint(1, 5)
        return self._points

    def reset(self):
        new_x = random.randint(0, constants.MAX_X - 1)
        new_y = random.randint(0, constants.MAX_Y - 1)
        self._position = Point(new_x, new_y)
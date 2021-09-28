import random

class Hider:

    """
    The hider class is used to generate a random number for the hider location as well
    as a list to keep track of the distance between the most recent seeker location
    the hider location. The class also creates and returns the hint variable to be
    printed in the console class.
    """

    def __init__(self):
        """
        defines two variables for a hider location and a list of distance
        changes between the hider and the seeker.
        """
        self.location = random.randint(1, 1000)
        self.distance = [1000]

    def get_hint(self):
        """
        evaluates the last distance list value and determines if it is closer
        to the hider or not and returns the hint to be printed in the console
        """
        if self.distance[-1] == 0:
            hint = "You found me! Thank you for playing!"
        elif self.distance[-1] < self.distance[-2]:
            hint = "You're getting warmer..."
        elif self.distance[-1] > self.distance[-2]:
            hint = "You're getting colder..."

        return hint


    def watch(self, location):
        """
        calculates the new distance between the seeker and the hider by
        accepting the seeker location and subracting the absolute value.
        This value is then appended to the distance list
        """
        new_location = int(abs(location - self.location))
        self.distance.append(new_location)
        
        
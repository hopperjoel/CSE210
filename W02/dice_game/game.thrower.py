import random

# TODO: Define the Thrower class here.

class Thrower():
    """A thrower is the part of the program responsible for the state of the dice.
        The thrower manages all of the functions for throwing dice, determining points
        from the current roll, and determining whether or not the game can be continued.
    """
    def __init__(self):
        self.die_1 = 0
        self.die_2 = 0
        self.die_3 = 0
        self.die_4 = 0
        self.die_5 = 0

        self.dice = [self.die_1, self.die_2, self.die_3, self.die_4, self.die_5]
        self.num_throws = 0
        
    #Variables for each die?
    def throw_dice(self, throw_status):
        #Function for Throwing Dice by generating a random number between 1 and 6?
            #Returns array of random numbers?
        """
        This function receives the throw_status boolean and generates random integers between 1 and 6, then creates a list
        of all the obtained integers for each die variable, then returns the list of integers
        """
        if throw_status:
            self.die_1 = random.randint(1, 6)
            self.die_2 = random.randint(1, 6)
            self.die_3 = random.randint(1, 6)
            self.die_4 = random.randint(1, 6)
            self.die_5 = random.randint(1, 6)
            self.dice = [self.die_1, self.die_2, self.die_3, self.die_4, self.die_5]
            self.num_throws += 1

        return self.dice, self.num_throws
    
    def get_points(self, dice):
    #Function for getting the current points?
        #counts the number of 1s and 5s and sums the total?
        #returns the sum
        """
        This function calculates the score for this current roll by accepting the list of 
        randomly generated integers (or dice) and determining the total points for the round
        by adding 1's and 5's. It returns this total amount of points.
        """
        self.points = 0
        for i in dice:
            if i == 1:
                self.points += 100

            if i == 5:
                self.points += 50

        return self.points
    
    def can_throw(self, points, num_throws):
    #Function to determine if a 1 or a 5 were thrown and if the player can continue
        #returns a boolean for keep_playing?
        """
        This function determines whether or not the game can be continued by checking the obtained 
        total points score for that round (since rolling a 5 or a 1 would produce points). It
        returns a boolean value of throw_status
        """
        if points > 0 or num_throws == 0:
            self.throw_status = True
        else:
            self.throw_status = False

        return self.throw_status


    

    



    
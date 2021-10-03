import random

# TODO: Define the Board class here
class Board:

    def __init__(self):
        self._piles = {}
        self.__prepare = 0

    def apply(self):
        pass

    def is_empty(self):
        pass
    
    def to_string(self):
        pile_num = random.randint(2, 5)
        for i in range(pile_num):
            pile_list = []
            stone_count = random.randint(1, 9)
            while stone_count > 0:
                pile_list.append(0)
                stone_count -= 1
            self._piles[i] = pile_list
        
        

    # def set_prepare(self, value):
    #     self.__prepare = value

    # def get_prepare(self):
    #     return self.__prepare

    # prepare_prop = property(get_prepare, set_prepare)
import random


_piles = {}

def to_string():
    pile_num = random.randint(2, 5)
    for i in range(0, pile_num - 1):
        pile_list = ""
        stone_count = random.randint(1, 9)
        for j in range(stone_count):
            pile_list += " 0"
        _piles[i] = pile_list
    print(_piles)
    for i in range(pile_num):
        
to_string()
"""
Match Coins Game, Coin class
Ryma Djoudad
Class representing tossable coin that lands on either heads or tails
No starter code 
03/14/2026
"""
import random
class coin:

    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        toss_decison = random.randint(0, 1)
        if toss_decison == 0:
            self.__sideup = "Heads"
        elif toss_decison == 1:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup
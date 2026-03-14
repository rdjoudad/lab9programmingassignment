"""
Match Coins Game, Player class
Ryma Djoudad
Class representing player that has name, wallet and coin object
No starter code 
03/14/2026
"""
from coin import Coin

class Player:


    def __init__(self, name, wallet, coin):
        self.__name = "Player 1"
        self.__wallet = 20
        self.__coin = Coin()
"""
Match Coins Game
Ryma Djoudad
Determining a winner based on a coin game made with classes that interact
No starter code 
03/14/2026
"""

from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"Player 1 has {player1.get_wallet()} coins")
    print(f"Player 2 has {player2.get_wallet()} coins")

    input("Do you want to toss the coins? (y/n) ")
    while input == "y" or "Y":
        player1.toss_coin()
        player2.toss_coin()

    side1 = player1.get_coin_toss
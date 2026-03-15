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

    answer = input("Do you want to toss the coins? (y/n) ")
    while answer == "y" or answer == "Y":
        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"Player 1 tossed {side1}")
        print(f"Player 2 tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a match! Player 1 wins a coin.")
        else:
            player1.lose_coin()
            player2.win_coin()
            print("...No match! Player 2 wins a coin.")

        print(f"Player 1 has {player1.get_wallet()} coins.")
        print(f"Player 2 has {player2.get_wallet()} coins.")
    
    answer = input("Do you want to toss the coins? (y/n) ")

    print("---Final Score---")
    print(f"Player 1: {player1.get_wallet()}")
    print(f"Player 2: {player2.get_wallet()}")

    

main()






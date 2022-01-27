from player import Player
from dealer import Dealer

def main():
    """
    The main function creates a player and a dealer and then instructs the dealer to begin playing the game.
    """

    # Define the player
    player = Player()
    # Define the dealer
    dealer = Dealer(player)
    # Tell the dealer to play the game
    dealer.play_game()
    

if __name__ == "__main__":
    main()    
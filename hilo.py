from player import Player
from dealer import Dealer

def main():
    """
    The main function creates a player and a dealer and then instructs the dealer to begin playing the game.
    """

    player = Player()
    dealer = Dealer(player)
    dealer.play_game()
    

if __name__ == "__main__":
    main()    
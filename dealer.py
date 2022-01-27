from player import Player
from card import Card

class Dealer:
"""
Dealer - This class holds information about the dealer and controls play of the game, like a dealer would if this game was played physically.
"""

    def __init__(self, Player):
        """
        __init__(self, Player) -- This function identifies and sets the initial values for this class
        """
        self.card1_value = 0
        self.card2_value = 0
        self.hilo_choice = ""
        self.settle_score = 0
        self.player = Player
    
    def play_game(self):
        cards = Card()
        play = Player()
            
        
                
           
                
        
            

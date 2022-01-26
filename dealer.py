from player import Player
from card import Card
"""
Dealer - This class holds information about the dealer and controls play of the game, like a dealer would if this game was played physically.
"""

class Dealer:

    def __init__(self, Player):
        self.card1_value = 0
        self.card2_value = 0
        self.hilo_choice = ""
        self.settle_score = 0
        self.player = Player
    
    def play_game(self):
        cards = Card()
        play = Player()
            
        
                
           
                
        
            

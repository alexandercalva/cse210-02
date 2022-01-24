"""
Dealer - This class holds information about the dealer and controls play of the game, like a dealer would if this game was played physically.
"""

class Dealer():

    def __init__(self, Player):
        self.card1_value = 0
        self.card2_value = 0
        self.hilo_choice = ""
        self.player = Player

   
        

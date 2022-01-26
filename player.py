"""
Player - This class holds information about the player's score and allows the dealer to update his score.
"""

class Player():

    def __init__(self):
        self.score = 300
                
    
    def get_score(self, new_score):
         self.score += new_score
         return self.score  

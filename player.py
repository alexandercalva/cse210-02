"""
Player - This class holds information about the player's score and allows the dealer to update his score.
"""

class Player():

    def __init__(self):
        """
        __init__(self) -- This function identifies and sets the initial values for this class
        """
        self.score = 300
                   
    def win(self):
        self.score += 100

    def lose(self):
        self.score -= 75
        if self.score < 0:
            self.score = 0

    def get_score(self):
        return(self.score)
    

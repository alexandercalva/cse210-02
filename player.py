class Player():
    """
    Player - This class holds information about the player's score and allows the dealer to update his score.
    """

    def __init__(self):
        """
        __init__(self) -- This function identifies and sets the initial values for this class
        """
        self.score = 300
                   
    def win(self):
        """
        win is called when the player wins and 100 is added to the score.
        """
        self.score += 100

    def lose(self):
        """
        lose is called when the player loses and 74 is subtracted from the score.
        """
        self.score -= 75
        if self.score < 0:
            self.score = 0

    def get_score(self):
        """
        get_score returns the current player score
        """
        return(self.score)
    

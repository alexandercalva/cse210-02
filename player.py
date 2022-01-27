"""
Player - This class holds information about the player's score and allows the dealer to update his score.
"""

class Player():

    def __init__(self):
        self.score = 300
        self.current_card = 0
        self.next_card = 0
        self.score = 0
        self.choose_high_low = "" 
                
    
    def get_score(self, new_score):
         self.score += new_score
         return self.score  

        

    def player_win(self):
        self.score += 100

    



    def player_win_lose(self):
        if self.choose_high_low.lower() == "h": #if the player choose High we validate if the player is win or lose 
            if self.current_card < self.next_card:
                self.score += 100
            else:
                self.score -= 75
                if self.score <= 0:  # validate if the score is lower or iqual than 0 the Game is over
                    print("Game Over")
        #if the player choose is low we validate if the player is win or lose
        else:
            if  self.current_card > self.next_card:
                self.score += 100
            else:
                self.score -= 75
                if self.score <= 0:   # determine if the score is lower or iqual than 0 the Game is over
                    print("Game Over")


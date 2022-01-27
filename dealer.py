from card import Card

class Dealer:
    """
    Dealer - This class holds information about the dealer and controls play of the game, like a dealer would if this game was played physically.
    """

    def __init__(self, player):
        """
        __init__(self, Player) -- This function identifies and sets the initial values for this class
        """
        self.card = Card()
        self.card1_value = 0
        self.card1_suit = chr(9829)
        self.card2_value = 0
        self.card2_suit = chr(9829)
        self.hilo_choice = ""
        self.player = player
    
    def choose_hi_low(self):
        """
        choose_hi_low asks the player what the player guesses the next card will be.
        The player's choice is returned.
        """
        self.hilo_choice = input("Higher or Lower? [h/l] ")
        return (self.hilo_choice)

    def settle_score(self):
        """
        settle_score determines if the player correctly predicted whether the card was higer or lower.
        If the player guessed correctly, the player's score is incremented.
        If the player guessed incoreectly, the player's score is decremented.
        """
        if (self.card1_value < self.card2_value and self.hilo_choice == "h"):
            self.player.win()
        elif (self.card1_value > self.card2_value and self.hilo_choice == "l"):
            self.player.win()
        else:
            self.player.lose()

    def play_game(self):
        """
        play_game executes the game process in a loop until the player decides that he no longer wants to play or until his points reach 0
        """
        print("Welcome to HiLo!  Sit down and let's play! I will be your dealer. You start your game with 300 points.")
        play_again = "y"
        while(play_again == "y"):

            # Deal card 1
            self.card1_value = self.card.get_face_value()
            self.card1_suit = self.card.get_suit()
            print("The card is {} {}".format(self.card1_value, self.card1_suit))

            # Choose higher or lower
            self.hilo_choice = self.choose_hi_low()

            # Deal card 2
            self.card2_value = self.card.get_face_value()
            self.card2_suit = self.card.get_suit()
            print("The next card was {} {}".format(self.card2_value, self.card2_suit))

            # Determine results of the choice
            self.hilo_choice = self.settle_score()
            print("Your score is: ", self.player.get_score())

            if (self.player.get_score() > 0):
                play_again = input("Play again? [y/n] ")
            else:
                play_again = "n"

        if (self.player.get_score() > 0):
            print("Good game! You finished with a score of {}".format(self.player.get_score()))   
        else: 
            print("I am sorry.  You have lost all your points and the game is over.")
                
           
                
        
            

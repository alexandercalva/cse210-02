from random import randrange

class Card():
    """
    Card class holds information about the cards being delt.  Whenever requested, the class returns a random suit and face value.
    """

    def __init__(self):
        """
        __init__(self) -- This function identifies and sets the initial values for this class
        """
        self.suit = ''

    def get_face_value(self):
        """
        get_face_value returns a random face value (1 - 13) for the card requested.
        """
        return (randrange(1,13))

    def get_suit(self):
        """
        get_suit returns a random suit for the card requested.
        """
        suit = randrange(1,4)
        if suit == 1: 
            self.card_suit = chr(9829) #heart
        elif suit == 2: 
            self.card_suit = chr(9824) #spade
        elif suit == 3: 
            self.card_suit = chr(9827) #club
        else: 
            self.card_suit = chr(9829) #diamond        
        return(self.card_suit)

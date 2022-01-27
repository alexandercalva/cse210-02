from random import randrange

class Card():

    def __init__(self):
        """
        __init__(self) -- This function identifies and sets the initial values for this class
        """
        self.suit = ''

    def get_suit(self):
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
    
    def get_face_value(self):
        return (randrange(1,13))

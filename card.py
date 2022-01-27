from random import randrange

class Card():

    def __init__(self):
        """
        __init__(self) -- This function identifies and sets the initial values for this class
        """
        self.ini = 0

    def get_face_value(self):
        return (randrange(1,13))
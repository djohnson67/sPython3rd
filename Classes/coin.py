import random

#the coin class for flipping coins
class Coin:
    #__init__ initialize the sideup data with 'heads'
    def __init__(self):
        self.__sideup = 'Heads' #__ before name makes varaible private
        
    #generate a random number  0 = heads 1 = tails
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    #returns the value
    def get_sideup(self):
        return self.__sideup
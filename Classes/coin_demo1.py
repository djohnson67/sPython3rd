import random

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
    
def main():
    my_coin = Coin()

    print('This side up is ', my_coin.get_sideup())

    #toss the coin
    print('I am tossing the coin tens times...')
    for count in range(10):
        my_coin.toss()
        print('This side up is ', my_coin.get_sideup())


main()
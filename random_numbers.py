#displays a random number 1-100
import random

def main():
    for count in range(5):
        #get random
        number = random.randint(1,100)
        #display it
        print('The number is', number)

#call main
main()

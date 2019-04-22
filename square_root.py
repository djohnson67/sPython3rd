#demos the sq root function
import math

def main():
    #get a number
    number = float(input('enter a number: '))
    # get the square root
    square_root = math.sqrt(number)

    #result
    print('The square root of ', number, 'is ', square_root)

#call main
main()
#calculates the lenght of a right triangles hypotenuse
import math

def main():
    a = float(input('Enter the lenght of side A: '))
    b = float(input('Enter the lenght of side B: '))

    #calculate the length
    c = math.hypot(a,b)

    #display
    print('The lenght of the hypotenuse is: ', c)

main()
import circle
import rectangle

#CHOICE CONSTANCE
AREA_CIRCLE_CHOICE = 1
CIRCUMFRENCE_CIRCLE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

#msin
def main():
    #countrols loop and holds menu choice
    choice  = 0

    while choice != QUIT_CHOICE:
        display_menu()
        #get users's choice
        choice = int(input('Enter your choice: '))

        #perform action
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Enter the circles\'s radius: '))
            print('The area is ', circle.area(radius))
        elif choice == CIRCUMFRENCE_CIRCLE_CHOICE:
            radius = float(input('Enter the circle\'s radius: '))
            print('The circumfrence is ', circle.circumfrence(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input('Enter the rectangle\'s width: '))
            length = float(input('Enter the rectangle\'s length: '))
            print('The area is ',rectangle.area(width,length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input('Enter the rectangle\'s width: '))
            length = float(input('Enter the rectangle\'s length: '))
            print('The area is ',rectangle.perimeter(width,length))
        elif choice == QUIT_CHOICE:
            print('Exit the program')
        else:
            print('Error invalid choice')




#
#display menu
def display_menu():
    print('MENU')
    print('1) Area of a circle')
    print('2) Circumfrence of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')

#call main
main()
#assigns random nums to 2 dim array
import random

#consts for row and cols
ROWS = 3
COLS = 4

def main():
    #create array
    values = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    #fill list with randoms
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c ] = random.randint(1,100)
    #diplay results
    print(values)

main()

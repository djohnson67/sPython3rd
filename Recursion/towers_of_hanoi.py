def main():
    #setup init values
    num_discs = 3
    from_peg = 1
    to_peg = 3
    temp_peg = 2

    #play game
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('All discs moved')

    #displays disc moves to complete puzzle
def move_discs(num,from_peg, to_peg, temp_peg):
    if(num > 0):
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print('Move a disc from', from_peg, 'to peg', to_peg)
        move_discs(num - 1,temp_peg, to_peg, from_peg)

main()


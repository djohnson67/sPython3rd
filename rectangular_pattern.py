#displays rect pattern of asteriks
rows = int(input('How many rows? '))
cols = int(input('How manuy columns? '))

for r in range(rows):
    for c in range(cols):
        print('*',end='')
    print()
    

NUM_DAYS = 5

def main():
    #create list to hold sales
    sales = [0] * NUM_DAYS

    #index
    index = 0

    print('Enter the sales for each day: ')

    #get the sales
    while index < NUM_DAYS:
        print('Day # ',index + 1, ': ', sep='',end='')
        sales[index] = float(input())
        index+=1

    print('Here are the value u entered: ')
    for value in sales:
        print(value)

main()

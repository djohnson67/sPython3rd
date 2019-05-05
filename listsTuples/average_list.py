#calculates average from a list

def main():
    #create list
    score = [2.5, 7.3, 6.5, 4.0, 5.2]

    total = get_total(score)
    
    #get the avg
    average  = total / len(score)

    print('the average of the elements is ', average)

def get_total(value_list):
    #create the accumulator
    total = 0.0

    #get the sum total
    for value in value_list:
        total += value

    return total


main()
#calculates the sum of a series of numbers

max = 5 

#initialize the accumulator
total = 0.0

#explain what we're doing
print('This program calculates the sum of ')
print(max,' numbers you will enter')

#get nums and accumulate them
for counter in range(max):
    number = int(input('Enter a number: '))
    total += number

#display results
print('The total is ', total)

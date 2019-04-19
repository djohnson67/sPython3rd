#averages test scores - it asks for number of students and number of test scores

#get number of students
num_students = int(input('How many students do you have? '))

#get number of test score per student
num_test_scores = int(input('How many test scores per student?' ))

#determin each students average scre
for student in range(num_students):
    #init accumulator
    total = 0.0
    #get test score
    print('Student Number ', student+1)
    print('------------------')
    for test_num in range(num_test_scores):
        print('Test number ', test_num + 1, end='')
        score = float(input(': '))
        #add score to accumulator
        total += score;
    
    #calculate average
    average = total / num_test_scores

    #dissplay average
    print('The average for student number ', student + 1, \
        ' is: ', average)
    print()



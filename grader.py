#gets a numeric test score from the user and displays the letter grade
A_score = 90
B_score = 80
C_score = 70
D_score = 60

#get test score
score = int(input('Enter your test score: '))

#determine grade
if score >= A_score:
    print('Your grade is an A')
elif score >= B_score:
    print('Your grade is a B')
elif score >= C_score:
    print('Your grade is a C')
elif score >= D_score:
    print('Your grade is a D')
else:
    print('Your grade is an F')

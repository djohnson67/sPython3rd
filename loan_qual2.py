#determine if bank customer qualifies for loan
min_salary = 30000.0
min_years = 2

#get customers annual salary
salary = float(input('Enter annual salary: '))

#get number of yars on job
years_on_job = int(input('Enter number of years employed: '))

#determine if customer qualifes
if salary >= min_salary and years_on_job >= min_years:
        print('you qualify for the loan')
else:
    print('You do not qualify for the loan')
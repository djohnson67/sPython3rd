#determine if bank customer qualifies for loan
min_salary = 30000.0
min_years = 2

#get customers annual salary
salary = float(input('Enter annual salary: '))

#get number of yars on job
years_on_job = int(input('Enter number of years employed: '))

#determine if customer qualifes
if salary >= min_salary:
    if years_on_job >= min_years:
        print('you qualify for the loan')
    else:
        print('You must have been employed ', \
            'for at least ', min_years, \
            'years to qualify.')
else:
    print('You must earn at least $', \
            format(min_salary, ',.2f'), \
            ' per year to qualify.' , sep='')

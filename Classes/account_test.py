import bankaccount

def main():
    #get starting balan
    start_balance = float(input('Enter starting balance: '))

    #create account
    savings = bankaccount.BankAccount(start_balance)

    #deposit check

    pay = float(input('How much were you paid this week? '))
    print('I will deposit this into your account')
    savings.deposit(pay)

    #display balance
    print('Your account balance is $', format(savings.get_balance(), ',.2f'), sep='')

    #withdraw some cash
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account')
    savings.withdraw(cash)

    #display balance
    print('Your account balance is $', format(savings.get_balance(), ',.2f'), sep='')

    #test print function
    print(savings)

main()


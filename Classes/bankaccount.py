#simulate a bank account

class BankAccount:

    #__init__ method takes in initial balance
    def __init__(self, bal):
        self.__balance = bal
        
    #deposit
    def deposit(self, amount):
        self.__balance += amount
    
    #withdraw
    def withdraw(self, amount):
        if(self.__balance >= amount):
            self.__balance -= amount
        else:
            print('Error: Insufficient Funds')
    
    #get balance
    def get_balance(self):
        return(self.__balance)

    def __str__(self):
        return 'the  balance is $' + format(self.__balance, ',.2f')

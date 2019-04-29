#Luis Ruiz
#CS_232_Lab_13
# 25 April 2019

INTEREST_RATE = 0.02

class Account():
    def __init__(self, owner_name):
        self.owner = owner_name
        self.__balance = 0.00
        
    def get_balance(self):
        return round(self.__balance, 2)

    def deposit(self, deposit_amount):
        self.__balance += round(deposit_amount, 2)

    def withdrawal(self, withdrawal_amount):
        if(self.get_balance() < withdrawal_amount):
            print('insufficient funds')
            return False
        self.__balance -= round(withdrawal_amount, 2)
        return True

    def compare(self, account1):
        return(self.get_balance != account1.get_balance)

class Checking(Account):
    def __init__(self, owner_name):
        super().__init__(owner_name)
        

class Savings(Account):
    def __init__(self, owner_name):
        super().__init__(owner_name)
        self.__interest = INTEREST_RATE

    def interest(self):
        self.__balance *= round(self.__interest, 2)

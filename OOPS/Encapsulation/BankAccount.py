class BankAccount:
    def __init__(self , account_number):
        self.__account_number = account_number
        self.__balance = 0

    @property
    def get_account(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self , amount):
        self.__balance = amount
    
    def deposit(self , amount):
        if amount < 0:
            print('Invalid deposits')
        else:
            self.__balance += amount

    def withdraw(self , amount):
        if amount < 0:
            print('Invalid amount entry')
        elif amount > self.__balance:
            print('Insuffiecient funds')
            return
        else:
            self.__balance -= amount

acc = BankAccount("ABC123")
print(acc.balance)      
acc.deposit(5000)
print(acc.balance)       
acc.withdraw(6000)       
acc.deposit(-200)        
print(acc.balance)





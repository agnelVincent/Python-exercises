class Bank:
    accounts = set()
    def __init__(self , account_no , name):
        if account_no not in Bank.accounts:
            self.__account_no = account_no
            self.__name = name
            self.__balance = 0
            Bank.accounts.add(account_no)
        else:
            print('Account cannot be created.')
            return
        
    @property
    def balance(self):
        return self.__balance
    
    @property
    def account_no(self):
        return self.__account_no
      
    @property 
    def name(self):
        return self.__name
    
    def deposit(self , amount):
        if amount > 0:
            self.__balance += amount
        else:
            print('enter valid money')
    
    def withdraw(self , amount):
        if amount > self.__balance:
            print('insufficient balance')
            return
        else:
            self.__balance -= amount
            return amount
        

agnel = Bank("abc1", "Agnel")
print(agnel.balance)    
agnel.deposit(400)
print(agnel.balance)    
agnel.withdraw(200)
print(agnel.balance)    






        
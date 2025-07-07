class Employee:
    def __init__(self):
        self.__salary = 0

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self , amount):
        if amount < 0:
            print('Invalid salary')
            return 
        self.__salary = amount

    def apply_raise(self , percent):
        self.__salary *= (100+percent) / 100

    @property
    def tax(self):
        return self.__salary * 0.1
    
e = Employee()
e.salary = 15000
e.apply_raise(20)
print(e.salary)           # ➜ 18000
print(e.tax)              # ➜ 1800.0

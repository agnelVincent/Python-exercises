class Person:
    def __init__(self):
        self.__name = ''
        self.__age = 0

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self , s):
        if len(s) < 3:
            print('invalid name')
            return
        self.__name = s

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self , n):
        if n < 1 or n > 100:
            print('invalid age')
            return
        self.__age = n

    def is_adult(self):
        return self.__age >= 18
    

p = Person()
p.name = "Tony"
p.age = 17
print(p.is_adult())       # ➜ False
p.age = 121               # ➜ "Invalid age"

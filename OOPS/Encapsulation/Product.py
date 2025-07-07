class Product:
    def __init__(self , name):
        self.name = name
        self.__price = 0
        self.__discount = 0

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self , amount):
        if amount < 0:
            print('Price must be atleast 0')
            return
        self.__price = amount

    @property
    def discount(self):
        return self.__discount
    
    @discount.setter
    def discount(self , percentage):
        if percentage < 0 or percentage > 50:
            print('Invalid discount')
            return 
        self.__discount = percentage

    def final_price(self):
        return self.__price - (self.__price * (self.__discount / 100))
    

p = Product("Laptop")
p.price = 100000
p.discount = 10
print(p.final_price())    # ➜ 90000.0
p.discount = 60           # ➜ "Invalid discount"


    
class Vehicle:
    def __init__(self , brand):
        self.brand = brand

    def start(self):
        print('Vehicle starting')
        return
    
class Car(Vehicle):
    def __init__(self, brand , model):
        super().__init__(brand)
        self.model = model

    def start(self):
        super().start()
        print(f'Car {self.brand} {self.model} starting')
        return
    
v = Vehicle("Tata")
v.start()  

c = Car("Tesla", "Model S")
c.start()


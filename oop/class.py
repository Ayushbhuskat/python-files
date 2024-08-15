class Car :
    def __init__(self,brand,model) : #__init__ is a constructor 
        self.brand = brand #self means this (context)
        self.model = model

    def fullname(self): #classmethod
        return f"{self.brand} {self.model}"




my_car = Car("Toyota","hilux")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("tata","curv")
print(my_new_car.model)
print(my_new_car.brand)
print(my_car.fullname())
print(my_new_car.fullname())


class ElectricCar(Car) :
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model) #super means upperclass  
        self.battery_size = battery_size


my_tesla = ElectricCar("tesla","model s", "85kwh")  
print(my_tesla.model)
print(my_tesla.fullname())
     



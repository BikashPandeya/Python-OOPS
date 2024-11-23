class Car:
    def __init__(self , user_brand  ,user_model):
        self.brand = user_brand
        self.model = user_model

    def full_name(self):
        return f"{self.brand} {self.model}"  


class ElectricCar(Car):
    def __init__(self , brand  , model , battery_size ):
        super().__init__(brand , model)
        self.battery_size = battery_size



my_car = Car("Toyota" , "Supra")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name() , "\n\n")

my_new_car = Car("Maruti" , "Suzuki")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name() , "\n\n")


my_tesla = ElectricCar("Tesla" , "Model S" , "85kWh")
print(my_tesla.battery_size)
print(my_tesla.brand)
print(my_tesla.full_name())
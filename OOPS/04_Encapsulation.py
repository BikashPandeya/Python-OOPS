class Car:
    def __init__(self , user_brand  ,user_model):
        self.__brand = user_brand
        self.model = user_model

    def get_brand(self):
        return f"{self.__brand} !"    

    def full_name(self):
        return f"{self.__brand} {self.model}"  


class ElectricCar(Car):
    def __init__(self , brand  , model , battery_size ):
        super().__init__(brand , model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla" , "Model S" , "85kWh")
# print(my_tesla.__brand)     It will throw error because __ made brand attribute private and only accesible inside class and inheritance but not in object
print(my_tesla.get_brand())



# my_car = Car("Toyota" , "Supra")
# print(my_car.__brand)
# print(my_car.model)
# print(my_car.full_name() , "\n\n")

# my_new_car = Car("Maruti" , "Suzuki")
# print(my_new_car.__brand)
# print(my_new_car.model)
# print(my_new_car.full_name() , "\n\n")


# my_tesla = ElectricCar("Tesla" , "Model S" , "85kWh")
# print(my_tesla.battery_size)
# print(my_tesla.__brand)
# print(my_tesla.full_name())
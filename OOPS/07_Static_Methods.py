class Car:
    total_car = 0
    def __init__(self , user_brand  ,user_model):
        self.__brand = user_brand
        self.model = user_model
        Car.total_car += 1

    def get_brand(self):
        return f"{self.__brand} !"    

    def full_name(self):
        return f"{self.__brand} {self.model}" 

    def fuel_type(self):
        return "Petrol and Diesel" 
    
    def experiment(name):
        return f"{name} , Its an experiment ."
    
    @staticmethod
    def general_description(name):
        return f" {name } , Cars are best means of transportation"


class ElectricCar(Car):
    def __init__(self , brand  , model , battery_size ):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge" 




my_car = Car("Tesla" , "Model S")

print(my_car.general_description("Bikash"))

print(Car.general_description("Bikash"))

print(Car.experiment("Bikash"))



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
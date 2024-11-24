class Car:
    total_car = 0
    def __init__(self , user_brand  ,user_model):
        self.__brand = user_brand
        self.__model = user_model
        Car.total_car += 1

    def get_brand(self):
        return f"{self.__brand} !"    

    def full_name(self):
        return f"{self.__brand} {self.__model}" 

    def fuel_type(self):
        return "Petrol and Diesel" 
    
    def experiment(name):
        return f"{name} , Its an experiment ."
    
    @staticmethod
    def general_description(name):
        return f" {name } , Cars are best means of transportation"

    @property
    def model(self):
        return f"{self.__model} !"


class ElectricCar(Car):
    def __init__(self , brand  , __model , battery_size ):
        super().__init__(brand , __model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge" 




my_car = Car("Tesla" , "Model S")
# my_car.model = "Car"

print(my_car.model)
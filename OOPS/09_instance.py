class Car:
    def __init__(self , user_brand  ,user_model):
        self.__brand = user_brand
        self.model = user_model

    def get_brand(self):
        return f"{self.__brand} !"    

    def full_name(self):
        return f"{self.__brand} {self.model}" 

    def fuel_type(self):
        return "Petrol and Diesel" 


class ElectricCar(Car):
    def __init__(self , brand  , model , battery_size ):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge" 




my_tesla = ElectricCar("Tesla" , "Model S" , "85kWh")
print(isinstance(my_tesla , Car))
print(isinstance(my_tesla , ElectricCar))
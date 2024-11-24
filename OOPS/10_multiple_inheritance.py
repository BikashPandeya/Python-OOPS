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
    
    def car_class(self):
        return "THis is from \"Car\" class"


class ElectricCar(Car):
    def __init__(self , brand  , model , battery_size ):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge" 

    def electric_car_class(self):
        return "THis is from \"electric car\" class"




my_tesla = ElectricCar("Tesla" , "Model S" , "85kWh")
print(isinstance(my_tesla , Car))
print(isinstance(my_tesla , ElectricCar))

class Battery:
    def battery_info(self):
        return "This is from \"Battery\" class"

class Engine:
    def engine_info(self):
        return "This is from \"Engine\" class"
    

class ELectricCarTwo(Battery , Engine , Car):
    pass

multiple_inheritance = ELectricCarTwo("Tesla" , "Model alpha")
print(multiple_inheritance.battery_info())
print(multiple_inheritance.engine_info())
print(multiple_inheritance.car_class())

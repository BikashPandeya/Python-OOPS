class Car:
    def __init__(self , user_brand  ,user_model):
        self.brand = user_brand
        self.model = user_model

    def full_name(self):
        return f"{self.brand} {self.model}"   

my_car = Car("Toyota" , "Supra")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name() , "\n\n")

my_new_car = Car("Maruti" , "Suzuki")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())
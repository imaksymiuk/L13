#3. Create a Car class with the following attributes: brand, model, year, 
#and speed. The Car class should have the following methods: accelerate, 
#brake and display_speed. The accelerate method should increase the speed by 5, 
#and the brake method should decrease the speed by 5. 
#Remember that the speed cannot be negative.


class Car:
    def __init__(self, brand, model, year, speed = 0):
        self.brand = brand
        self.model = model
        self.year = year
        if speed < 0:
            self.speed = 0
        else: 
            self.speed = speed

    def accelerate(self):
        self.speed = self.speed + 5
        return self.speed
    
    def brake (self):
        if self.speed > 5:
            self.speed = self.speed - 5
        else:
            self.speed = 0
        return self.speed
    

car = Car('Audi', 'A7', 2021, -1)
print(car.brake())
class Vehicle ():
    def __init__(self,brand):
        self.brand=brand
        
class Gogoro(Vehicle):
    def __init__(self,brand,battery_health):
        super().__init__(brand)
        self.battery_health=battery_health
    

my_bike = Gogoro("Gogoro S2", "98%")
print(my_bike.brand)           
print(my_bike.battery_health)  

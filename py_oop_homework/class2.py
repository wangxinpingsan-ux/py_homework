class Vehicle():
    wheel=2
    def __init__(self,brand):
        self.brand=brand
    def drive(self):
        print(f"{self.brand}正在前進中...")
class Gogoro(Vehicle):
    def drive (self):
        print(f"{self.brand} 啟動了靜音加速模式！🤫")

my_bike1=Vehicle("三陽")
print(my_bike1.wheel)
my_bike1.drive()

my_bike2=Gogoro("Gogoro VIVA")
print(my_bike2.wheel)
my_bike2.drive()

my_bike3=Vehicle("BMW")
my_bike3.wheel=4
print(my_bike3.wheel)
my_bike3.drive()
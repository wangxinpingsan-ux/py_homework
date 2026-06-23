class Car():
    color=None

    def change_color (self,color):
        self.color=color

car1=Car()
print(car1.color)

car1.change_color ("white")
print(car1.color)
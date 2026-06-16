import math
radius=(float(input("enter radius")))

area=round((float(math.pi*radius**2)),3)
print(f"perimeter circle is {round(2*math.pi*radius,3)}")
print(f"area is {area}")
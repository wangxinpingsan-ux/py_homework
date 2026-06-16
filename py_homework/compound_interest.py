principal=0
rate=0
time=0
while principal<=0:
 principal=float(input("enter principal "))
 if principal<=0:
  print("the money must >0")
while rate<=0:
 rate=float(input("enter rate "))
 if principal<=0:
  print("the rate must >0")
while time<=0:
 time=float(input("enter time "))
 if time<=0:
  print("the time must >0")

print(f"total is {round(principal*(1+(rate/100))**time,2)}")














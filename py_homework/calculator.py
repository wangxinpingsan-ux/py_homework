calculator=input("enter symbol (+-*/)")

num1=(float(input("enter first number")))
num2=(float(input("enter second number")))

if calculator =="+":
 print(f"answer is {num1+num2}")
elif calculator =="-":
 print(f"answer is {num1-num2}")
elif calculator =="*":
 print(f"answer is {num1*num2}")
elif calculator =="/":
 print(f"answer is {num1/num2}")
else:
 print("error")
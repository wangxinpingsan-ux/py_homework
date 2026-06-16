num=(int(input("enter number (1 to 100)")))
while num<1 or num>100:
    print("error")
    num=(int(input("enter number (1 to 100)")))
print(f"your number is {num}")

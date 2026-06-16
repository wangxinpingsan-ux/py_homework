name=(str(input("enter your name ")))

if len(name)>12:
    print("too much")
elif " "in name:
    print("don't space")
    print (f"the {name.find(" ")+1} is space")
elif not name.isalpha():
 print("don't number")
else:
   print("ok")
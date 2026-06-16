weight=round((float(input("enter weight "))),2)
unit=(str(input("kg or lb"))).upper()
if unit =="KG":
    print (f"the lb is {round(weight*2.2,2)}")
elif unit=="LB":
    print (f"the kg is {round(weight/2.2,2)}")
else:
    print("error")
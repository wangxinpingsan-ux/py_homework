credit_number=(str(input ("enter credit number (16)")))
if len(credit_number)!=16:
    print("16 number!!")
elif credit_number.isalpha():
    print("only number")
else:
 first=credit_number[0:4]
 last=credit_number[-4:]
 print(f"{first}********{last}")

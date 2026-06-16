row=int(input("enter row "))
col=int(input("enter col "))
symbol=str(input("enter symbol "))

for i in range(row,0,-1):
    for j in range(col,0,-1):
        print(symbol,end="")
    print()


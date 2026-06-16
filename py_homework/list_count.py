how_many=int(input("how many number "))

num=[]

for i in range(0,how_many,1):
    num.append(input("enter number(123)"))
one=num.count("1")
two=num.count("2")
three=num.count("3")

print(f"1 have {one}\n2 have {two}\n3 have {three}")
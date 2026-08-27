num=list(map(int,input().split()))
num.reverse()
even=[]
total=0
for i in num:
    if i%2==0:
        even.append(i)
for i in even:
    total=i*i+total
print(total)

count=int(input("how many "))

#num=[None]*count
#for i in range(0,count,1):
  # num[i]=input("enter number ")
num=[]
for i in range(0,count,1):
   num.append(input("enter number "))#num.append() ()放入input("enter number ")

num.remove("1")

for i in range(0,len(num),1):
   print(num[i])



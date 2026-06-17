import random

answer=random.randint(1,100)



count=0
while 1 :
 x=int(input("enter number (1~100)"))
 count+=1
 if x<answer:
    print("大一點")
 elif x>answer:
    print("小一點")
 elif x==answer:
    print (f"正確\n答案為{answer}\n你猜{count}次")
    break
    
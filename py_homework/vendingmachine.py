menu={"漢堡":"100","薯條":"30","雞腿":"60","雞塊":"40","可樂":"30","紅茶":"15"}

for item , price in menu.items():
    print(f"{item}:{price}")

cart=[]  
total=0

while True:
    
    food=(input("enter food").lower())
    if food =="q":
        break
    elif menu.get(food) is None:
        print("商品不存在")
    else:
     cart.append(int(menu.get(food)))
    

total=sum(cart)

print(f"total is {total}")
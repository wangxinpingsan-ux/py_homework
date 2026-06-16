menu={"漢堡":"100","薯條":"30","雞腿":"60","雞塊":"40","可樂":"30","紅茶":"15"}

for item , price in menu.items():
    print(f"{item}:{price}")

cart=[]  
court=0
total=0

while True:
    
    food=(input("enter food"))
    if food =="q".lower():
        break
    cart.append(int(menu.get(food)))
    court+=1

for i in range(0,court,1):
  total=total+cart[i]

print(f"total is {total}")
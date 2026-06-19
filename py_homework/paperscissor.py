import random


computer=["剪刀","石頭","布"]
answer=random.choice(computer)


run=True


while run==True:
  player=input("出拳")
  if player ==answer :
    print("平手")
  elif player =="剪刀":
    if answer=="石頭":
        print("lose")
    if answer=="布":
        print ("win")
  elif player =="石頭":
    if answer=="布":
        print("lose")
    if answer=="剪刀":
        print ("win")
  elif player =="布":
    if answer=="石頭":
        print("剪刀")
    if answer=="石頭":
        print ("win")
  else :
    print("error")
  print(f"computer is {answer}")
  print(f"your is {player}")
  play=input("again?(y/n)")
  if play =="n":
   run=False
  elif play=="y":
    continue
  

       
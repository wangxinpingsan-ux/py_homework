import time
my_tiem=int(input("enter time (second) "))

for x in range(my_tiem, 0 ,-1):
    
    second=x%60
    minute=x//60
    print(f"{minute:02}:{second:02}")


    time.sleep(1)
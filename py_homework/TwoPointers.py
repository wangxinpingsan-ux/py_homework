num=list(map(int,input().split()))
target=int(input())


low,high=0,-1

while True:
    if num[low]+num[high]>target:
        high-=1
    elif num[low]+num[high]<target:
        low+=1
    else:
        break
print(f"[{low},{len(num)+high}]")




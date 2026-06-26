name=("wang","xin","ping")
num=(5,8,10)

total=zip(name,num)

print(list(total))
for i in zip(name,num):
    print(f"{i}",end="")

total_dict=dict(zip(name,num))

print(total_dict)

for i ,j in total_dict.items():
    print (f"{i}:{j}")
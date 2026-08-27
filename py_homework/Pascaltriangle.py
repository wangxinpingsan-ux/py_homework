n=5
all=[[0]*((2*n)+1) for i in range(1,n+1,1)]
all[0][n]=1
for i in range ((2*n)+1):
    print(all[0][i],end="")
print()
for i in range(n-1):
    print("0",end="")
    
    for j in range((2*n)-1):
        print(all[i][j]+all[i][j+2],end="")
        all[i+1][j+1]=all[i][j]+all[i][j+2]
    print("0",end="")
    print()




    















#for i in range(1,n+1,1):
#    print(space*(n-i),end="")
#    if i==1:
#        print(num)
#    else:
#        for j in range(0,(2*i)-1,1):
#        
#            print(i,end="")
#    print()
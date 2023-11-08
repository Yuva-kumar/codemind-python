n=int(input())
for i in range(n+1,1,-1):
    s=''
    for j in range(1,i):
        s+=str(j)
    print(s)
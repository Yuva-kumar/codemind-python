a,b=map(int,input().split())
for i in range(1,b+1,2):
    b=str(a)+' x '+str(i)+' = '+str(i*a)
    print(b)
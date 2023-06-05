m,n=list(map(int,input().split()))
lst=list(map(int,input().split()))
l=[]
for i in lst:
    a=str(abs(i))
    b=len(a)
    l.append(int(b)) 
c=0
for i in l:
    if i==n:
        c+=1
print(c)
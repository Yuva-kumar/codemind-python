n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    a=str(abs(i))
    b=len(a)
    l.append(int(b)) 
c=0
a=max(l)
for i in l:
    if i==a:
        c+=1
print(c)
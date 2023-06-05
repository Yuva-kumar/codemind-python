n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    a=str(abs(i))
    b=len(a)
    l.append(int(b))
print(*l)
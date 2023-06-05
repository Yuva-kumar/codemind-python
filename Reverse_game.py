n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    a=str(i)
    b=int(a[::-1])
    l.append(b)
print(*l)
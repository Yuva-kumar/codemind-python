n=int(input())
lst=list(map(int,input().split()))
l=[]
a=len(lst)
b=sum(lst)
d=b//a
for i in lst:
    if i<=d:
        l.append(i)
        
print(len(l))

n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    l.append(str(i))
# print(l)
l1=[]
for i in l:
    l1.append(len(i))
a=max(l1)
l2=[]
for i in l:
    if len(i)==a:
        l2.append(i)
print(*l2)
    


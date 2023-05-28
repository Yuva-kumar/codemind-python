n=int(input())
arr=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in arr:
    if i%2==0:
        l1.append(i)

for i in arr:
    if i%2!=0:
        l2.append(i)
for i in l1:
    l3.append(i)
for i in l2:
    l3.append(i)
print(*l3)

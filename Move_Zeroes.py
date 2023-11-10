n=int(input())
arr=list(map(int,input().split()))
l=[]
l1=[]
for i in arr:
    if i!=0:
        l.append(i)
    else:
        l1.append(i)
print(*(l+l1))
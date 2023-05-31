n,k=map(int,input().split())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i%k!=0:
        l.append(i)
print(len(l))
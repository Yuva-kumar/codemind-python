n=int(input())
arr=list(map(str,input().split()))
c=0
for i in arr:
    if len(i)%2==0:
        c+=1
print(c)
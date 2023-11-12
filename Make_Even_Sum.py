n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if i%2!=0:
        c+=1
if c==0:
    print(1)
elif c%2==0:
    print(1)
else:
    print(0)
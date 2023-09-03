n=int(input())
arr=list(map(int,input().split()))
if n%2==0:
    l=[]
    for i in range(n):
        l.append(arr[i])
    print(*l)
else:
    l=[]
    for i in range(n):
        l.append(arr[i])
    l.append(0)
    print(*l)
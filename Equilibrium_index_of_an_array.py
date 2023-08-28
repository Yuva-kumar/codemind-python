a1=int(input())
for i in range(a1):
    n=int(input())
    arr=list(map(int,input().split()))
    a=n//2
    b=arr[0:a]
    c=arr[a+1:]
    if sum(b)==sum(c):
        print(a)
    else:
        print(-1)
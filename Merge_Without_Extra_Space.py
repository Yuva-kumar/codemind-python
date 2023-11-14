for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    arr1=list(map(int,input().split()))
    l=arr+arr1
    l.sort()
    print(*l)
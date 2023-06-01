n=int(input())
arr=list(map(int,input().split()))
a=n//2
b=n-a
c=arr[:a]
if n%2!=0:
    d=arr[b-1:]
    print(sum(c))
    print(sum(d))
    
else:
    d=arr[b:]
    print(sum(c))
    print(sum(d))
        
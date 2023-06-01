n=int(input())
arr=list(map(int,input().split()))
a=n//2
b=n-a
c=arr[:a]
if n%2!=0:
    d=arr[b-1:]
    e=sum(c)
    f=sum(d)
    print(abs(e-f))
else:
    d=arr[b:]
    e=sum(c)
    f=sum(d)
    print(abs(e-f))
        
        
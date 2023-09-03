n=int(input())
arr=list(map(int,input().split()))
if n%2==0:
    a=n//2
    b=arr[:a]
    c=arr[a:]
    d=c[::-1]
    l=[]
    
    for i in range(len(b)):
        l.append(b[i])
        l.append(d[i])
    print(*l)
else:
    a=n//2
    b=arr[:a+1]
    c=arr[a+1:]
    d=c[::-1]
    d.append(0)
    l=[]
    
    for i in range(len(b)):
        l.append(b[i])
        l.append(d[i])
    print(*l)
n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
x=max(arr)
l=[]
for i in range(a,b+1):
    l.append(i)
if x in l:
    print(-1)
else:
    print(x)
    
    
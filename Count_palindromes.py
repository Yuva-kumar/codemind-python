def pal(n):
    a=str(n)
    b=a[::-1]
    c=int(b)
    if n==c:
        return True
    else:
        return False
n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if pal(i):
        c+=1
print(c)
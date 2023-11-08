def prime(n):
    if n<2:
        return False
    a=int(n**0.5)
    for i in range(2,a+1):
        if n%i==0:
            return False
    return True
n=int(input())
arr=list(map(int,input().split()))
c=1
d=1
for i in arr:
    if prime(i):
        c*=i
    else:
        d*=i
print(abs(c-d))
        
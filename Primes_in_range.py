def prime(n):
    a=int(n**0.5)
    if n<2:
        return False
    for i in range(2,a+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if prime(i):
        c+=1
print(c)
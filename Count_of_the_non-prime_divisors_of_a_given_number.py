def prime(n):
    a=int(n**0.5)
    if n<2:
        return False
    for i in range(2,a+1):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i)==False:
            c+=1
print(c)
        
    
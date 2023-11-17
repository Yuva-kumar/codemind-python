def prime(n):
    a=int(n**0.5)
    if n<2:
        return False
    for i in range(2,a+1):
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n):
    print('prime')
else:
    print('not a prime')
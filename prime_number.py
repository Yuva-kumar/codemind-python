import math
def fun(n):
    a=math.sqrt(n)
    b=int(a)
    for i in range(2,b+1):
        if n%i==0:
            return False
    return True
n=int(input())
fun(n)
if fun(n):
    print('prime')
else:
    print('not a prime')
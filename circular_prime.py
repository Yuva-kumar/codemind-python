import math
def prime(n):
    a=int(math.sqrt(n))
    if n <= 1:
        return False
    for i in range(2,a+1):
        if n%i ==0:
            return False
    return True
k = input()
c = k[::-1]
if prime(int(k)) and prime(int(c)):
    print('circular prime')
elif prime(int(k)) and prime(int(c)) == False:
    print('prime but not a circular prime')
else:
    print('not prime')

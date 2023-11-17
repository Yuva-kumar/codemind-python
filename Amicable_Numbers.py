n=int(input())
m=int(input())
c,d=0,0
for i in range(1,(n//2)+1):
    if n%i==0:
        c+=i
for i in range(1,(m//2)+1):
    if m%i==0:
        d+=i
if (c==m) and (d==n):
    print('Amicable')
else:
    print('Not Amicable')
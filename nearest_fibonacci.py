def fib(n):
    lst=[0,1]
    for i in range(2,n+5):
        val=lst[i-1]+lst[i-2]
        lst.append(val)
    return lst
n=int(input())
l=fib(n)
l1=[]
l2=[]
for i in l:
    if i>n:
        l1.append(i)
    elif i<n:
        l2.append(i)
a=l1[0]
b=l2[-1]
c=abs(n-a)
d=abs(n-b)
s=[]
if c>d:
    print(b)
elif c==d:
    s.append(b)
    s.append(a)
    for i in s:
        print(i, end=' ')
else:
    print(a)
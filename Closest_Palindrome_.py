def pal(n):
    a=str(n)
    if n!=(int(a[::-1])):
        return False
    else:
        return True
n=int(input())
l=[]
l1=[]
l2=[]
for i in range(n*2):
    if pal(i):
        l.append(i)
for i in l:
    if i<n:
        l1.append(i)
    elif i>n:
        l2.append(i)
a=l1[-1]
b=l2[0]
if abs(n-a)>abs(n-b):
    print(b)
elif abs(n-a)==abs(n-b):
    print(a,b)
else:
    print(a)
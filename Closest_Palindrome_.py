def pal(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=int(input())
l=[]
for i in range(0,(n*2)+100):
    if pal(i):
        l.append(i)
l1,l2=[],[]
for i in l:
    if i<n:
        l1.append(i)
    elif i>n:
        l2.append(i)
a=abs(l1[-1]-n)
b=abs(l2[0]-n)
if a==b:
    print(l1[-1],l2[0])
elif a>b:
    print(l2[0])
else:
    print(l1[-1])


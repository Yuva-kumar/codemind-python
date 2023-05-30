n=int(input())
lst=list(map(int,input().split()))
l=[]
a=lst[::2]
b=len(a)
for i in a:
    if i%2==0:
        l.append(i)
c=len(l)
if b==c:
    print('True')
else:
    print('False')
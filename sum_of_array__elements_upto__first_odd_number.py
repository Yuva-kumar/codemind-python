n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i%2!=0:
        l.append(i)
b=l[0]
c=arr.index(b)
d=arr[:c]
a=len(l)
if a==0:
    print('0')
elif c==0:
    print('0')
else:
    print(sum(d))

n=int(input())
l=list(map(int,input().split()))
a=l[0::2]
b=l[1::2]
s=''
for i in range(len(a)):
    s+=(b[i]*(" "+str(a[i])))
ab="0,1,2,3,4,5,6,7,8,9"
l1=[]
for i in s:
    if i in ab:
        l1.append(i)
l2=[]
for i in l1:
    l2.append(int(i))
print(*l2)
    
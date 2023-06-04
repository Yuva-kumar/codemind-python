n=int(input())
lst=list(map(int, input(). split()))
l=[]
for i in lst:
    if i%2==0:
        l.append(i)
b=len(l)
if b==0:
    print(sum(lst))
else:
    a=l[0]
    b=lst.index(a)
    c=lst[:b]

    print(sum(c))
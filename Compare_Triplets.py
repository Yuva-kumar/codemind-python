l=list(map(int,input().split()))
l1=list(map(int,input().split()))
c,d=0,0
for i in range(len(l)):
    if l[i]>l1[i]:
        c+=1
    elif l1[i]>l[i]:
        d+=1
print(c,d)

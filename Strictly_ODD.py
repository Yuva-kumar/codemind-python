n=int(input())
lst=list(map(int,input().split()))
l=[]
l1=[]
l2=[]
for i in lst:
    if i%2!=0:
        l.append(i)
for i in l:
    l1.append(lst.index(i))
a=len(l1)
for i in l1:
    if i%2!=0:
        l2.append(i)
b=len(l2)
if a==b:
    print('True')
else:
    print('False')
        
    

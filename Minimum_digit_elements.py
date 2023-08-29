n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    l.append(str(i))
# print(l)
l1=[]
for i in l:
    l1.append(len(i))
c=0
for i in l1:
    if i==min(l1):
        c+=1
print(c)
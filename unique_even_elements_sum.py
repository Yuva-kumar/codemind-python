n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i not in l:
        l.append(i)
c=0
for i in l:
    if i%2==0:
        c+=i
print(c)
        
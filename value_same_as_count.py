n=int(input())
arr=list(map(int,input().split()))
s={}
for i in arr:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
l=[]
for i in s:
    l.append(i)
l1=[]
for i in s.values():
    l1.append(i)
c=0
for i in range(0,len(l)):
    if l[i]==l1[i]:
        c+=1
print(c)
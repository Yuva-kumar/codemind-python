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
    l.append(s[i])
c=0
for i in l:
    c+=(i//2)
print(c)
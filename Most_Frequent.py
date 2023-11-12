n=int(input())
arr=list(map(int,input().split()))
s={}
for i in arr:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
l=[s[i] for i in s]
a=max(l)
l1=[i for i in s if s[i]==a]
print(min(l1))

    
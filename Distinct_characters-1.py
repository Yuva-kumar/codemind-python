n=input().lower()
a="abcdefghijklmnopqrstuvwxyz"
s={}
for i in n:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
l=[]
for i  in s:
    if s[i]==1:
        l.append(i)
l.sort()
s=''
for i in l:
    if i in a:
        s+=i
print(s)
        
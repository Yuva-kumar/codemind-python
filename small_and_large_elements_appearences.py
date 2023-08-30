n=input()
a="abcdefgghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
l=[]
for i in n:
    if i in a:
        l.append(i)
c=min(l)
d=max(l)
s={}
for i in l:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
print(c,s[c],d,s[d])
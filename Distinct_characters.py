a=input().lower()
b="abcdefghijklmonopqrstuvwxyz"
l=[]
for i in a:
    if i not in l:
        l.append(i)
l.sort()
s=''
for i in l:
    if i in b:
        s+=i
print(s)
    

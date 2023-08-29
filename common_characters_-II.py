a=input().lower()
b=input().lower()
c="abcdefghhhhhhijklmnopqrstuvwxyz"
l=[]
for i in a:
    if i  in b:
        l.append(i)
for i in b:
    if i  in a:
        l.append(i)
l1=[]
for i in l:
    if i in c:
        l1.append(i)
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(len(l2))

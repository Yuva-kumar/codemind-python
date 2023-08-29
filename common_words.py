a=input().lower().split()
b=input().lower().split()
l=[]
for i in b:
    if i in a:
        l.append(i)
        
print(*l)
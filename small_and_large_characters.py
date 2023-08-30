n=input().split()
l=[]
for i in n:
    l.append(min(i))
    l.append(max(i))
print(*l)
    
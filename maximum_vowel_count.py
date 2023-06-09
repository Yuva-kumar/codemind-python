n=input().split()
c,l=0,[]
for i in n:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
            l.append(c)
print(max(l))
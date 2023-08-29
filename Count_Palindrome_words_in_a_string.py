n=input().lower().split()
c=0
for i in n:
    if i[::-1]==i:
        c+=1
print(c)
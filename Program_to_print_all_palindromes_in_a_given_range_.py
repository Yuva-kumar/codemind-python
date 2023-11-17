n=int(input())
m=int(input())
c=[]
for i in range(n,m+1):
    if str(i)==str(i)[::-1]:
        c.append(i)
print(*c)
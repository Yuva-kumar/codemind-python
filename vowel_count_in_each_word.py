n=input()
a=n.split()
for i in a:
    c=0
    for j in i:
        if j in "aeiouAEIOU":
            c+=1
    print(c,end=' ')
    
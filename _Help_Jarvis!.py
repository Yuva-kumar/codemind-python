for _ in range(int(input())):
    n=input()
    l=[]
    for i in n:
        l.append(int(i))
    l1=[i for i in range(min(l),max(l)+1)]
    c=0
    for i in  l1:
        if str(i) not in n:
            c+=1
    if c!=0:
        print('NO')
    else:
        print('YES')
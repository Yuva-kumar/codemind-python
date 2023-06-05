n=input()
b=len(n)
a=[]
for i in n:
    if i not in a:
        a.append(i)
c=len(a)
if c==b:
    print('True')
else:
    print('False')
    
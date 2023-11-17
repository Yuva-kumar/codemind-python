n=input()
l=[]
for i in n:
    l.append(int(i))
b=len(l)
a=list(set(l))
if b==len(a):
    print('Unique Number')
else:
    print('Not Unique Number')
n=input()
lst=[]
l=[]
for i in n:
    if i in "aeiouAEIOU":
        l.append(i)
for i in l:
    if i not in lst:
        lst.append(i)
l2=[]
for i in "aeiou":
    if i not in lst:
        l2.append(i)
if len(l2)!=0:
    print(*l2)   
else:
    print('0')


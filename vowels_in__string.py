n=input()
lst=[]
l=[]
for i in n:
    if i in "aeiouAEIOU":
        l.append(i)
for i in l:
    if i not in lst:
        lst.append(i)
print(*lst)
        

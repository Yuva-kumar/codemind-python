n=input()
a=n.split()
l=[]
k="aeiouAEIOU"
c=0
for i in a:
    if (i[0] in k) and (i[-1] not in k):
        c+=1
print(c)
        
    
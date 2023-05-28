n=int(input())
lst=list(map(int,input().split()))
a=len(lst)
l=[]
l1=[]
l2=[]
l3=[]
l4=[]
for i in lst[::-1]:
    l.append(i)
for j in range(0,a):
    l2.append(j)
for i in l2:
    l3.append(2**i)
r = [a * b for a, b in zip(l, l3)]
print(sum(r))
        
        
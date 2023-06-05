n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    while i:
        r=i%10
        i=i//10
        l.append(r)
print(sum(l))
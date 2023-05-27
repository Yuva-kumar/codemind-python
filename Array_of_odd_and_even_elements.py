n=int(input())
arr=list(map(int,input().split()))
l=[]

for i in arr:
    if i%2!=0:
        l.append(i)
for j in arr:
    if j%2==0:
        l.append(j)
# for ele in l: 
#     if ele == l[-1]:
#         print(ele)
#     else:
#         print(ele, end = ' ')
print(*l)
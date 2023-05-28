n=int(input())
arr=list(map(int,input().split()))
l=[]
c=0
for i in arr:
    if i==0 or i==1:
        c+=1
if c==len(arr):
    print('True')
else:
    print('False')
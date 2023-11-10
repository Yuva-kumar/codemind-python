n=int(input())
arr=list(map(int,input().split()))
l=[]
l1=[]
a=0
for i in range(0,len(arr)-1,2):
    l.append(arr[i])
    l1.append(arr[i+1])
if abs(sum(l)-sum(l1))%4==0:
    print('X')
else:
    print('Y')
        
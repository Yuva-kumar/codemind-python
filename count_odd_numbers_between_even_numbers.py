n=int(input())
lst=list(map(int,input().split()))
prev,pre,nxt,count=0,1,2,0
for i in range(n-2):
    if lst[prev+i]%2==0 and lst[pre+i]%2!=0 and lst[nxt+i]%2==0:
        count+=1
print(count)
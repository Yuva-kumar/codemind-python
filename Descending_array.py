def asc(n):
    prev,pre=0,1
    l=[]
    for i in range(0,n-1):
        if lst[prev+i] <= lst[pre+i]:
            return False
    return True
n=int(input())
lst=list(map(int,input().split()))
if asc(n):
    print('yes')
else:
    print('no')

            
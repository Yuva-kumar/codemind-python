n=int(input())
arr1=list(map(int,input().split()))
arr=[]
for i in arr1:
    if i not in arr:
        arr.append(i)
if len(arr)<3:
    print(max(arr))
else:
    arr.sort()
    arr=arr[::-1]
    print(arr[2])
    
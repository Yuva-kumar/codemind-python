for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]+arr[j]) in arr:
                c+=1
    if c==0:
        print(-1)
    else:
        print(c)
            
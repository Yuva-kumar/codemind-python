for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(n):
        a=arr[:i]
        b=arr[i+1:]
        if sum(a)==sum(b):
            print('YES')
            break
    else:
        print('NO')
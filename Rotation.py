for _ in range(int(input())):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    k=b%len(arr)
    x=arr[:len(arr)-b]
    y=arr[len(arr)-b:]
    print(*(y+x))
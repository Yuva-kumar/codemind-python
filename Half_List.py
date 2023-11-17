n=int(input())
arr=list(map(int,input().split()))
l=arr[:(n//2)]
l1=arr[(n//2):][::-1]
print(*(l1+l))

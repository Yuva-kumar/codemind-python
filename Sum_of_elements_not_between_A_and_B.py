l=int(input())
arr=list(map(int,input().split()))
n,m=map(int,input().split())
count = 0
for i in arr:
    if n > i or i > m:
        count += i
print(count)
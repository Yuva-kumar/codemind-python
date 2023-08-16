def fib(n):
    lst=[0,1]
    for i in range(2,n):
        pre=lst[i-1]+lst[i-2]
        lst.append(pre)
    return lst
n=int(input())
lst=fib(n)
print(*lst)
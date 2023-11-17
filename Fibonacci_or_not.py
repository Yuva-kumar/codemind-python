def fib(n):
    l=[0,1]
    for i in range(n):
        l.append(l[-1]+l[-2])
    return l
n=int(input())
a=fib(n)
if n in a:
    print('True')
else:
    print('False')


        
    
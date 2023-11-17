
def fun(n):
    l=[]
    a=n**0.5
    b="{:.1f}".format(a)
    if str(a)==b:
        return True
    else:
        return False
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if fun(i):
        c+=i
print(c)
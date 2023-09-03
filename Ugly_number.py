n=int(input())
if n==1:
    print('Ugly Number')
else:
    while n%2==0:
        n//=2
    while n%3==0:
        n//=3
    while n%5==0:
        n//=5
    if n==1:
        print('Ugly Number')
    else:
        print('Not Ugly Number')
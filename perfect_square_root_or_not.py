n=int(input())
a=n**0.5
b="{:.1f}".format(a)
if str(a)==b:
    print('True')
else:
    print('False')
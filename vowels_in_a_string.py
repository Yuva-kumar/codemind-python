n=input()
m=input()
for i in n:
    if m in n:
        print('True')
        print(n.index(m))
        break
    else:
        print('False')
        break
    
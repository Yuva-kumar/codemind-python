a=input().split()
cnt, lst = 0, []
for i in a:
    cnt = 0
    for j in i:
        if j in 'aeiouAEIOU':
            cnt += 1
    lst.append(cnt)
            
print(min(lst))
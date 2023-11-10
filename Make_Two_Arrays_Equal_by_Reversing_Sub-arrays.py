n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr1=list(map(int,input().split()))
c=0
for i in arr:
    if i not in arr1:
        c+=1
if c==0:
    print('True')
else:
    print('False')
# s={}
# for i in arr:
#     if i not in s:
#         s[i]=1
#     else:
#         s[i]+=1
# s1={}
# for i in arr1:
#     if i not in s1:
#         s1[i]=1
#     else:
#         s1[i]+=1
# if s==s1:
#     print('True')
# else:
#     print('False')
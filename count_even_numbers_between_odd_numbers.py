n = int(input())
arr = list(map(int, input(). split()))
prev, at, nxt, count = 0, 1, 2, 0
for i in range(n - 2):
    if arr[prev + i] % 2 == 1 and arr[at + i] % 2 == 0 and arr[nxt + i] % 2 == 1:
        count += 1
print(count)
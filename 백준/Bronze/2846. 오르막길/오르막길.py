N = int(input())

arr = list(map(int, input().split()))
start = arr[0]
max_val = 0

for i in range(1, N):
    if arr[i - 1] < arr[i]:
        dif = arr[i] - start
        if max_val < dif:
            max_val = dif
    else:
        dif = 0
        start = arr[i]

if max_val < dif:
    max_val = dif

print(f"{max_val}")
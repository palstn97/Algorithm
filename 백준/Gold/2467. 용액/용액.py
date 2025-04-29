N = int(input())
arr = list(map(int, input().split()))

i = 0
j = N - 1
arr.sort()
min_val = float('inf')

while i < j:
    if arr[i] + arr[j] == 0:
        lst = [arr[i], arr[j]]
        break

    if arr[i] + arr[j] > 0:
        if min_val > abs(arr[i] + arr[j]):
            lst = [arr[i], arr[j]]
            min_val = abs(arr[i] + arr[j])
        j -= 1

    else:
        if min_val > abs(arr[i] + arr[j]):
            lst = [arr[i], arr[j]]
            min_val = abs(arr[i] + arr[j])
        i += 1


print(*lst)
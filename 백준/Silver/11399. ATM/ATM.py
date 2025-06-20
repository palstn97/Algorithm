N = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0
for i in range(N):
    sum = 0
    for j in range(i + 1):
        sum += arr[j]
    result += sum

print(result)
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = arr[-1]
new_sum = 0

for i in range(len(arr)):
    new_sum += ((arr[i] / M) * 100)

result = new_sum / len(arr)
print(result)
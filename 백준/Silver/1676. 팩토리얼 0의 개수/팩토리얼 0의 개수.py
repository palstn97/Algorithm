N = int(input())
mul = 1
for i in range(1, N + 1):
    mul *= i

find_zero = str(mul)
result = 0
for j in range(len(find_zero) - 1, 0, -1):
    if find_zero[j] == '0':
        result += 1
    else:
        break

print(result)
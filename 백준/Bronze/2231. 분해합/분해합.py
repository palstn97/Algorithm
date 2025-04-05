N = int(input())

lst = []
for i in range(1, N + 1):
    n_sum = i + sum(map(int, str(i)))
    if N == n_sum:
        lst.append(i)

if lst:
    print(lst[0])
else:
    print(0)
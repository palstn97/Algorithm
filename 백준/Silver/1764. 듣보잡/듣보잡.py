N, M = map(int, input().split())
arr1 = set(input() for _ in range(N))
arr2 = set(input() for _ in range(M))

lst = sorted(arr1 & arr2)

print(len(lst))
for k in lst:
    print(k)
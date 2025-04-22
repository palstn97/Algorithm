from itertools import permutations

N, M = map(int, input().split())

arr = list(map(int, input().split()))
lst = []
for permutation in permutations(arr, 3):
    if sum(permutation) <= M:
        lst.append(sum(permutation))

lst.sort()
print(lst[-1])


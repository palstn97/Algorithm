from itertools import combinations

N = int(input())
num = []
for i in range(1, 11):
    for c in combinations(range(10), i):
        num.append(int(''.join(map(str, sorted(c, reverse=True)))))

num.sort()

if N <= len(num):
    print(num[N - 1])
else:
    print(-1)

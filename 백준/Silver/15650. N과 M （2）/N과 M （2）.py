from itertools import combinations

N, M = map(int, input().split())
lst = []
for i in range(1, N + 1):
    lst.append(i)

comb = combinations(lst, M)

for c in comb:

    print(*c)


'''
from itertools import combinations

N, M = map(int, input().split())

# 1부터 N까지 리스트
lst = list(range(1, N + 1))

# combinations 객체 ([] 없이!)
comb = combinations(lst, M)

# 하나씩 꺼내서 출력
for c in comb:
    print(*c)  # * 붙여서!

# 또는
from itertools import combinations

N, M = map(int, input().split())

# 바로 for문
for comb in combinations(range(1, N+1), M):
    print(*comb)
'''

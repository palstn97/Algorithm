from itertools import permutations

# 순열 사용하기!
N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()  # 사전순으로 출력이니까 정렬이 필요하다.
permutation = permutations(lst, M)

for i in permutation:
    print(*i)
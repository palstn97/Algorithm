from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 바로 set로 씌우면 중복된 건 다 제거가 된다. 그래서 순열 구하고 set로 감싸기
res = set(permutations(arr, M))
res = sorted(res)   # 사전순으로 정렬을 한다.

for i in res:
    print(*i)
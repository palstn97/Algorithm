import sys
input = sys.stdin.readline

# 카운팅 정렬 사용해보기
N = int(input())
lst = [0] * 10001   # 1 ~ 10000 범위니까

# 각 숫자의 개수 세기
for _ in range(N):
    num = int(input())
    lst[num] += 1

# 개수만큼 출력하기
for i in range(10001):
    if lst[i] > 0:
        for _ in range(lst[i]):
            print(i)
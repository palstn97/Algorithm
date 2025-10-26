import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 1. 번호 -> 이름
num_to_name = {}
# 2. 이름 -> 번호
name_to_num = {}

for i in range(1, N + 1):
    name = input().rstrip()
    num_to_name[i] = name
    name_to_num[name] = i

for _ in range(M):
    q = input().rstrip()
    if q.isdigit():  # 숫자인 경우
        print(num_to_name[int(q)])
    else:   # 이름인 경우
        print(name_to_num[q])
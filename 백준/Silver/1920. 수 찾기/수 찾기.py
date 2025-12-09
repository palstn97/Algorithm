# list로 받으면 시간 초과
# 이때 B는 list로 받아야함. 중복된거가 제거되지 않으려면
N = int(input())
A = set(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)
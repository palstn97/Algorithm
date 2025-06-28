import sys
input = sys.stdin.readline    # 입력을 받을 때 느리니까 설정하기

N, M = map(int, input().split())
arr1 = list(map(int, input().split()))

pre_sum = [0] * (N + 1) # 누적합을 미리 구하는 리스트 하나 생성
for i in range(1, N + 1):
    pre_sum[i] = pre_sum[i - 1] + arr1[i - 1]   # 누적합을 구하는 과정
for _ in range(M):
    i, j = map(int, input().split())
    result = pre_sum[j] - pre_sum[i - 1]    # 특정 구간의 합
    print(result)
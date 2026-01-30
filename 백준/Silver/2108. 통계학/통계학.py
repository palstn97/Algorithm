from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

print(round(sum(arr)/N))

arr.sort()
print(arr[N//2])

count = Counter(arr)    # Counter로 빈도수를 계산하는데 이건 딕셔너리 형태가 된다.
max_cnt = max(count.values())   # 최대 빈도수를 구해야 하니까 딕셔너리의 벨류값 찾아서 최댓값 구하기
cnt = []
for k, v in count.items():   # (숫자, 빈도수) 쌍을 꺼낸다.
    if v == max_cnt:    # 빈도수가 최대이면 그 숫자를 추가하자
        cnt.append(k)
# 최빈값이 여러개일 수도 있으니까 정렬하기
cnt.sort()
print(cnt[1] if len(cnt) > 1 else cnt[0])   # 최빈값이 여러개일 경우 처리

print((max(arr) - min(arr)))
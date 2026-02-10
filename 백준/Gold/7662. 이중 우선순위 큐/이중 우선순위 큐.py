'''
힙 두 개를 사용하기.
min_heap은 최솟값 찾는 용도
max_heap은 최댓값 찾는 용도
삭제된 원소를 찾는것은 딕셔너리를 사용해보자
'''
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []   # 최댓값용 -> 음수를 저장 -> 파이썬의 heapq는 min heap(가장 작은 값이 항상 맨 위에 있는 힙)만 지원하기 때문에 max heap을 위해서는 음수 처리가 필요하다.
    cnt = defaultdict(int)  # 각 숫자의 개수

    for _ in range(k):
        op, n = input().split()
        n = int(n)  # 다시 정수형으로 저장

        if op == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)    # 음수로 저장
            cnt[n] += 1

        else:
            if n == 1:  # 최댓값 삭제하기
                while max_heap and cnt[-max_heap[0]] == 0:  # 맨 위에 이미 삭제된 값이 있으면 계속 제거하기
                    heapq.heappop(max_heap)
                if max_heap:    # 최댓값 삭제하고 카운트 감소시기키기
                    max_val = -heapq.heappop(max_heap)
                    cnt[max_val] -= 1
            else:
                # 최솟값 삭제하기
                while min_heap and cnt[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    cnt[min_val] -= 1
    
    while min_heap and cnt[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and cnt[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if min_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")
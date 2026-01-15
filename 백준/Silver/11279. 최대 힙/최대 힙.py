import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []   # 최소 힙 -> 이건 최대 힙으로 사용할 예정이다.
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, -x)    # 음수로 변환하기. 왜? 일단은 최소 힙을 사용하니까 음수를 사용하면 최대가 되겠지?
                                    # 예를 들면 3, 1, 2가 원래 값이면 음수 변환하면 -3, -1, -2가 될거다. 근데 최소 힙에서는 -3이 가장 작지만 실제로는 3이 가장 크다! -> -를 없애면.
    elif x == 0:
        if heap:
            print(-heapq.heappop(heap)) # -처리를 해줬으니 다시 원상태로 돌리려면 다시 -를 붙여줘야한다.
        else:
            print(0)
# 이 문제에서 핵심은 최댓값을 뽑아내는건데 heapq를 사용하면 최소 힙이 된다. 하지만 -를 붙여주면 그 값이 실제로는 최대가 된다는 것이다!
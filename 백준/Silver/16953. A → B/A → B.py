'''
역방향 연산
visited가 필요없다. -> 항상 값이 감소하기 때문에 같은 값을 두 번 방문하지 않는다.
탐색 공간이 좁다. -> b에서 a로 가면서 계속 값이 줄어든다.
가지치기가 쉽다. -> now < A 면 바로 종료된다!
'''
from collections import deque

# 역방향 연산을 해서 B에서 A로 연산을 할거다!
A, B = map(int, input().split())

def bfs():
    q = deque([(B, 1)]) # (현재 수, 연산 횟수)

    while q:
        now, cnt = q.popleft()
        if now == A:
            return cnt

        if now < A:
            continue

        # 2로 나누기(짝수인 경우에만)
        if now % 2 == 0:
            q.append((now // 2, cnt + 1))

        # 끝자리가 1이면 제거하기
        if now % 10 == 1:
            q.append((now // 10, cnt + 1))  # 반드시 튜플로 감싸야하는거 잊지 말것!

    return -1

print(bfs())
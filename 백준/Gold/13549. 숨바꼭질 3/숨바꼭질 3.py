'''
가중치를 고려한 BFS 또는 다익스트라로 풀면 된다.
왜? 최소 시간을 원하기 때문이다. 그리고 현재 위치에서 다음 위치로 이동을 시킬거니까 이건 그래프이다.
기존의 일반적인 bfs와는 달리 이 문제는 0초랑 1초 후라는 시간이 있기 때문에 가중치가 다르다. 이는 다익스트라 또는 0-1 BFS이다.
가중치가 0과 1뿐이면 0-1BFS가 다익스트라에 비해 훨 빠르다.
그래서 2가지 경우로 나누는데 0초가 걸리는 순간이동은 deque의 앞쪽에 배치하고 1초가 걸리는 걷기는 뒤쪽에 배치를 한다.
그 이유는 시간이 적게 걸리는 경우를 먼저 놔야 더 빨리 처리하기 때문이다.
그리고 bfs니까 visited가 필요하겠지? 다만 visited[x]라고 하면 x에 도달하는 최소 시간을 의미하는 것이다.
'''
from collections import deque

N, K = map(int, input().split())

def bfs():
    visited = [-1] * 100001
    q = deque()
    q.append(N)
    visited[N] = 0  # 수빈이의 위치니까 걸리는 시간은 0초일 것이다.

    while q:
        x = q.popleft()
        # 동생이 있는 곳에 도착하면??
        if x == K:
            return visited[x]
        
        # 이제 두 가지, 아니 세세하게 생각하면 세 가지 케이스로 나눈다.
        nx = x * 2
        if 0 <= nx <= 100000 and visited[nx] == -1:
            visited[nx] = visited[x]    # 시간이 안걸린다
            q.appendleft(nx)    # 더 먼저 처리할 수 있도록 앞쪽에 추가
        
        # 걸을 때의 경우. 이때는 뒤에다가 추가한다.
        nx = x - 1
        if 0 <= nx <= 100000 and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            q.append(nx)
        
        nx = x + 1
        if 0 <= nx <= 100000 and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            q.append(nx)

    return visited[K]   # 동생의 위치에서의 visited값을 반환하기

print(bfs())
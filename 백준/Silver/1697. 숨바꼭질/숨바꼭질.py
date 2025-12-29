from collections import deque
import sys
input = sys.stdin.readline

def bfs(N, K):
    q = deque([(N, 0)])   # 현재 위치, 걸린 시간
    visited = [False] * 100001
    visited[N] = True

    while q:
        pos, time = q.popleft()

        # 동생 위치에 도달
        if pos == K:
            return time
        
        # 3가지 이동 방법
        for n_pos in (pos - 1, pos + 1, pos * 2):
            if 0 <= n_pos <= 100000 and not visited[n_pos]:
                visited[n_pos] = True
                q.append((n_pos, time + 1))

N, K = map(int, input().split())
res = bfs(N, K)
print(res)
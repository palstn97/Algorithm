from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    if a == b:
        return ''
    visited = [None] * 10000
    visited[a] = ''    # 시작점 표시
    q = deque([a])

    while q:
        cur = q.popleft()

        # 4가지 연산하기
        for next_num, op in [((cur * 2) % 10000, 'D'), ((cur - 1) % 10000, 'S'), ((cur % 1000) * 10 + cur // 1000, 'L'), ((cur % 10) * 1000 + cur // 10, 'R')]:
            if visited[next_num] == None: # 방문 안했으면?
                visited[next_num] = visited[cur] + op
                if next_num == b:
                    return visited[next_num]
                q.append(next_num)

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))

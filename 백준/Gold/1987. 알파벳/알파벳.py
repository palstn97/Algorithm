'''
최장 경로를 찾아야하고 같은 위치라도 경로마다 방문한 알파벳이 다르기 때문에 bfs가 아닌 dfs를 활용한 백트래킹으로 풀어야한다.
bfs는 한 번 방문하면 끝이기 때문에 같은 위치의 알파벳이라도 방문한 알파벳 집합이 다른 경우를 처리하기 어렵다.
그래서 dfs를 활용한 백트래킹을 사용해서 접근을 해야한다.
모든 가능한 경로를 탐색하고 각 경로마다 방문한 알파벳 집합을 관리하면서 최댓값을 계속 갱신해준다.
'''
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]

# 델타 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 방문한 알파벳 저장
visited_alphabet = set()

def dfs(r, c, cnt): # r, c는 현재 위치이고 cnt는 현재까지 지나온 칸 수를 의미한다.
    max_cnt = cnt

    # 가지치기: 알파벳은 최대 26개
    if cnt == 26:
        return 26

    # 델타 탐색 진행
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            next_alphabet = grid[nr][nc]
            # 아직 방문하지 않았다면??
            if next_alphabet not in visited_alphabet:
                visited_alphabet.add(next_alphabet) # set이기 때문에 .add 사용 -> 선택
                max_cnt = max(max_cnt, dfs(nr, nc, cnt + 1))    # 재귀 결과와 비교하기
                visited_alphabet.remove(next_alphabet)  # 취소(백트래킹) -> remove를 해줌으로써 다른 경로에서 같은 알파벳을 다시 사용할 수 있다.
                # 백트래킹이 없다면 visited에 있는 경우 그 경로를 다시 못 가기에 모든 경로를 탐색하지 못한다.

    return max_cnt

visited_alphabet.add(grid[0][0])    # (0, 0)에서 시작!
ans = dfs(0, 0, 1)

print(ans)
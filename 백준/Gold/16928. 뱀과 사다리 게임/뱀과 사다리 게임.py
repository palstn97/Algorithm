from collections import deque

N, M = map(int, input().split())
# 리스트로 받는것도 좋지만 코테에서는 시간복잡도가 너무 커져서 시간 초과가 날 수 있다. 그렇기에 딕셔너리로 푸는 연습을 하자!
board = {}  # 뱀과 사다리를 구분할 필요가 없다. 어짜피 어디로 이동하는지만 알면 되니까!

for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(M):
    a, b = map(int, input().split())
    board[a] = b

def bfs():
    q = deque([1])  # 첫 번째 칸이 들어가고
    visited = [-1] * 101
    visited[1] = 0  # 1번 칸은 횟수가 0 -> visited는 지금까지의 횟수를 저장하는 것이다.

    while q:
        current = q.popleft()
        
        if current == 100:
            return visited[100]
        for i in range(1, 7):   # 주사위 1부터 6까지
            next_pos = current + i  # 다음 위치
            if next_pos > 100:
                continue
            if next_pos in board:   # 뱀이나 사다리를 만난 경우
                next_pos = board[next_pos]
            if visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                q.append(next_pos)
    return -1

print(bfs())
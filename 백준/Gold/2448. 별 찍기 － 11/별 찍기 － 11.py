import sys
input = sys.stdin.readline

def star(n, row, col):  # 크기 n삼각형의 왼쪽 위 꼭짓점을 (row, col)에 맞춰서 그려라!
    # 초기: n = 3이면 직접 그리기
    if n == 3:
        grid[row][col + 2] = '*'
        grid[row + 1][col + 1] = '*'
        grid[row + 1][col + 3] = '*'
        for i in range(5):
            grid[row + 2][col + i] = '*'
        return
    half = n // 2

    # 위쪽 삼각형: 중앙 위에 배치
    star(half, row, col + half)
    # 아래 왼쪽 삼각형
    star(half, row + half, col)
    # 아래 오른쪽 삼각형 -> half 삼각형의 밑변 너비는 2 * half - 1 = n - 1이고 그 다음 칸인 col+n부터 시작된다.
    star(half, row + half, col + n)

N = int(input())
# 그리드 초기화 -> 공백으로 채우고, 높이는 N이고 너비는 2 * N - 1이다. 규칙에 따르면!
grid = [[' '] * (2 * N - 1) for _ in range(N)]
# (0, 0)부터 크기 N 삼각형 그리자
star(N, 0, 0)

for r in grid:
    print(''.join(r))
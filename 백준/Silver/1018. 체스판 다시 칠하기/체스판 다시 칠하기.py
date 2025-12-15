N, M = map(int, input().split())
mat = [list(map(str, input())) for _ in range(N)]

min_cnt = 64    # 최대로 칠할 수 있는 개수 설정

# 시작 행과 열로 모든 경우 탐색 -> 브루트포스
for start_i in range(N - 7):
    for start_j in range(M - 7):
        cnt_w = cnt_b = 0   # 카운터 초기화 -> 흰색으로 시작하는 패턴으로 맞출 때 칠할 개수, 검은색으로 시작하는 패턴으로 맞출 때 칠할 개수
        # 8x8 체스판 내부의 각 칸을 순회
        for i in range(8):
            for j in range(8):
                # 짝수 위치면 시작 색, 홀수 위치면 반대 색 -> (0, 0), (0, 1), (1, 0), (1, 1)
                if (i + j) % 2 == 0:
                    if mat[start_i + i][start_j + j] != 'W':
                        cnt_w += 1
                    if mat[start_i + i][start_j + j] != 'B':
                        cnt_b += 1
                else:
                    if mat[start_i + i][start_j + j] != 'B':
                        cnt_w += 1
                    if mat[start_i + i][start_j + j] != 'W':
                        cnt_b += 1
        min_cnt = min(min_cnt, cnt_w, cnt_b)    # 가장 최소인 경우가 답

print(min_cnt)
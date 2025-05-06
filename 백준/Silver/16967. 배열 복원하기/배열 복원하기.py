H, W, X, Y = map(int, input().split())

arr_B = [list(map(int, input().split())) for _ in range(H + X)]
arr_A = [[0] * W for _ in range(H)]
for r in range(H):
    for c in range(W):
        # 만약에 두 개가 겹친다면? -> 현재의 위치가 x,y 이상인 경우가 겹치는 경우
        if r >= X and c >= Y:
            arr_A[r][c] = arr_B[r][c] - arr_A[r - X][c - Y]
            # 그 외에는 그대로
        else:
            arr_A[r][c] = arr_B[r][c]

for i in arr_A:
    print(' '.join(map(str, i)))
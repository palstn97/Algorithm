def magnetic(mat):
    num = 0
    for c in range(100):
        found_N = False
        for r in range(100):
            if mat[r][c] == 1:
                found_N = True
            if mat[r][c] == 2:
                if found_N:
                    num += 1
                    found_N = False
    return num


for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    print(f"#{tc} {magnetic(matrix)}")
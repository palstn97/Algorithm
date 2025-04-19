def sudoku(mat):
    for i in range(9):
        # 열을 검사하는 리스트와 행을 검사하는 리스트를 생성하자
        row_lst = [0] * 10
        col_lst = [0] * 10
        for j in range(9):
            row = mat[i][j]  # row 부분 -> i번째 행 , j 번째 열 -> i가 고정, j가 움직이기 때문에 행을 구하려면 이렇게 하기 -> 가로 검사
            col = mat[j][i]  # col 부분 -> 마찬가지로 열을 구하기 위해서 열 부분을 고정시키기 -> 세로 검사
            if row_lst[row] == 1:
                return 0
            else:
                row_lst[row] = 1
            if col_lst[col] == 1:
                return 0
            else:
                col_lst[col] = 1

            if i % 3 == 0 and j % 3 == 0:   # 3x3 부분 검사하기 위해서 진행 -> 3의 배수가 되는 부분만 확인해주면 될것
                box_lst = [0] * 10
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        num = mat[r][c]
                        if box_lst[num] == 1:
                            return 0
                        else:
                            box_lst[num] = 1
    return 1


T = int(input())

for tc in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    print(f"#{tc} {sudoku(matrix)}")
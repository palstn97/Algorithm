import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 곱셈 함수
def mul(mat1, mat2):
    n = len(mat1)
    result = [[0] * n for __ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000

    return result

def power(mat, num):
    m = len(mat)

    if num == 1:
        return [[mat[i][j] % 1000 for j in range(m)] for i in range(m)]
    
    if num % 2 == 0:
        half = power(mat, num // 2)
        return mul(half, half)  # 행렬끼리 곱하기
    
    if num % 2 == 1:
        half = power(mat, num // 2)
        temp = mul(half, half)
        return mul(temp, mat)
    
result = power(A, B)
for r in result:
    print(' '.join(map(str, r)))
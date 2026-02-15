import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 곱셈 함수
def mul(mat1, mat2):    # 두 개의 행렬을 받는 함수 정의
    n = len(mat1)
    result = [[0] * n for _ in range(n)]    # 0으로 채워진 2차원 리스트 -> 여기에 곱셈된 결과를 담아줄 것

    for i in range(n):
        for j in range(n):
            for k in range(n):  # 곱셈을 위한 중간 인덱스
                result[i][j] += mat1[i][k] * mat2[k][j] # mat1의 i번째 행과 mat2의 j번째 열의 내적
            result[i][j] %= 1000    # k루프가 끝난 후 연산하기

    return result

def power(mat, num):    # 행렬 거듭제곱 함수
    m = len(mat)

    if num == 1:    # 재귀 종료 조건
        return [[mat[i][j] % 1000 for j in range(m)] for i in range(m)]
    
    if num % 2 == 0:
        half = power(mat, num // 2)
        return mul(half, half)  # 행렬끼리 곱하기
    
    if num % 2 == 1:
        half = power(mat, num // 2)
        temp = mul(half, half)  # half x half 계산하기 -> 예를 들어 A^4 x A^4
        return mul(temp, mat)   # A를 앞에 곱하기! 그러면 홀수인 경우 행렬의 거듭 제곱이 계산된다.
    
result = power(A, B)
for r in result:    # 각 행을 순회한다!
    print(' '.join(map(str, r)))

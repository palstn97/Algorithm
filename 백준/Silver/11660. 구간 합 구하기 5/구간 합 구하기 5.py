'''
누적합을 사용??
반복적인 구간의 합 계산을 빠르게 하고 싶다면 누적합을 사용하면 된다.
매번 for문을 돌린다면 한 쿼리당 O(N)이 소요되고 쿼리가 많을수록 느려진다.
그렇다면 누적합의 핵심 아이디어는??
"처음부터 여기까지의 합"을 미리 계산하자!!
prefix[i] = arr[0]부터 arr[i-1]까지의 합
즉 arr[L] - arr[R]까지의 합은?
=> (처음부터 R까지의 합) - (처음부터 L-1까지의 합) => prefix[R + 1] - prefix[L]

그렇다면 2차원 누적합은?
prefix[i][j] = (1, 1)부터 (i, j)까지의 직사각형 영역 합
prefix[i][j] = 현재 칸 + 위쪽 누적합 + 왼쪽 누적합 - 중복 제거 = arr[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
구간 합 구하기 -> answer = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 0번 행, 열을 0으로 패딩 -> 누적합을 계산할 때 i-1, j-1을 자주 쓰는데 i=1 또는 j=1이면 0번째를 접근해야 한다. 패딩을 하면 경계 처리를 깔끔하게 할 수 있기에 이렇게 설정!
grid = [[0] * (N + 1)]
for _ in range(N):
    row = [0] + list(map(int, input().split()))
    grid.append(row)

# 누적합 배열 -> prefix[i][j] = (1,1)부터 (i,j)까지 왼쪽 위 직사각형 전체 합
prefix = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix[i][j] = (grid[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1])

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = (prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])    # 전체 - 위 - 왼쪽 + 겹친 부분
    print(result)
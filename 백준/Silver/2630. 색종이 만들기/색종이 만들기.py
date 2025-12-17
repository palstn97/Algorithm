'''
분할 정복을 사용할 것인데 분할 정복은 큰 문제를 여러 개의 작은 문제들로 나눠서 해결하는 것이다!
그래서 이 문제에서는 나는 재귀를 사용해서 분할 정복 문제를 해결할 것이다.
재귀 함수가 인자로 받을 것은 시작 위치와 영역의 크기이다.
이때 재귀 함수가 하는 역할은 현재 영역이 모두 같은 색인지 판단을 하고 같으면 카운트하고 종료하고 다르면 그 영역을 4등분 해서 다시 재귀를 호출하는 것이다.
그렇다면 종료 조건은? -> 영역이 모두 같은 색이거나 크기가 1인 경우 종료이다.
'''

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def paper(x, y, size):
    global white, blue
    color = field[x][y] # 현재 영역의 첫 번째 칸 색깔 저장

    # 영역이 모든 같은 색인지 확인하는 과정
    for i in range(x, x + size):
        for j in range(y, y + size):
            if field[i][j] != color:
                half = size // 2
                paper(x, y, half)
                paper(x, y + half, half)
                paper(x + half, y, half)
                paper(x + half, y + half, half)
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1

paper(0, 0, N)
print(white)
print(blue)
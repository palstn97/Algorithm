N, r, c = map(int, input().split())

def z(N, r, c):
    # 1 * 1인 경우
    if N == 0:
        return 0
    
    # 현재 단계에서의 한 사분면의 크기
    half = 2 ** (N - 1)

    # 어느 사분면인지 확인하고 재귀 돌리기
    # 사분면 내부로 들어갈 때 좌표를 상대 좌표로 변환하기! -> 오른쪽이면 c - half / 아래쪽이면 r - half
    if r < half and c < half:
        return z(N - 1, r, c)
    elif r < half and half <= c < 2 ** N:
        return half * half + z(N - 1, r, c - half)
    elif half <= r < 2 ** N and c < half:
        return 2 * half * half + z(N - 1, r - half, c)
    else:
        return 3 * half * half + z(N - 1, r - half, c - half)
    
print(z(N, r, c))
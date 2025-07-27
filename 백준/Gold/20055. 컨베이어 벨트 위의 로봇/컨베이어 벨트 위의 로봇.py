N, K = map(int, input().split())
arr = list(map(int, input().split()))
robots = [False] * N

cnt = 0

while True:
    cnt += 1
    # 한 칸 회전
    arr = [arr[-1]] + arr[:-1]
    robots = [False] + robots[:-1]  # 회전 후 0번 자리는 비우기
    robots[-1] = False  # 로봇 내리는 위치면 바로 제거

    # 로봇 이동
    for i in range(N - 2, -1, -1):
        if robots[i] and not robots[i + 1] and arr[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            arr[i + 1] -= 1
    robots[-1] = False  # 내리는 위치에서는 항상 로봇 제거

    # 로봇 올리기
    if arr[0] > 0:
        robots[0] = True
        arr[0] -= 1

    # 내구도 0인 칸 수 세기
    if arr.count(0) >= K:
        print(cnt)
        break
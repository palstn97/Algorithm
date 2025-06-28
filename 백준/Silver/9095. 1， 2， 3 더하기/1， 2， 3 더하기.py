T = int(input())
for _ in range(T):
    n = int(input())
    if n == 1:  # 조건에 따라서 다르게 설정하기! 다른 방법은 그냥 DP[0] * max(4, n + 1)해서 최소 4칸을 확보하는 방법도 존재
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        DP = [0] * (n + 1)
        DP[1], DP[2], DP[3] = 1, 2, 4
        for i in range(4, n + 1):
            DP[i] = (DP[i - 3] + DP[i - 2] + DP[i - 1])
        print(DP[n])    # 위치 조심하기. 밖에 빼면 1, 2, 3일 때도 출력이 되면서 출력 2번 발생
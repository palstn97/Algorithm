# while 사용하지 말기 -> 사용하면 런타임에러 뜬다!
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = []
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in money:
        lst.append(N // i)
        N = N - (i * (N // i))

    print(f"#{tc}")
    print(f"{' '.join(map(str, lst))}")
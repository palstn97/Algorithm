def retire(day, money):
    global max_money

    if day > N:
        return

    max_money = max(max_money, money)
    if day < N:    # 오늘 상담을 선택하는 경우
        retire(day + work[day][0], money + work[day][1])

    retire(day + 1, money)  # 오늘 선택하지 않고 내일로 넘기기


N = int(input())
work = [list(map(int, input().split())) for _ in range(N)]
max_money = 0
retire(0, 0)
print(max_money)
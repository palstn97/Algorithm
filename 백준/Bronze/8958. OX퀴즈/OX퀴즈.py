T = int(input())
for _ in range(T):
    answer = input()
    total = 0   # 전체 점수를 기록하는 변수
    score = 0   # 연속된 점수를 기록하는 변수
    for i in answer:
        if i == 'O':
            score += 1
            total += score
        else:
            score = 0

    print(total)
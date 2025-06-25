T = int(input())

for _ in range(T):
    N = int(input())
    dic = {}
    for i in range(N):
        cloth = list(input().split())
        if cloth[1] not in dic:
            dic[cloth[1]] = [cloth[0]]  # 단어를 담을거니까 리스트 형식으로 만들어주기
        else:
            dic[cloth[1]].append(cloth[0])  # 존재하면 그 리스트에 담아주기

    cnt = 1 # 경우의 수 -> (종류1 + 1) * (종류2 + 1)...

    for key in dic:
        cnt *= (len(dic[key]) + 1)
    result = cnt - 1    # 전체에서 1을 빼줘야지만 답
    print(result)
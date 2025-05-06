T = int(input())

for tc in range(1, T + 1):
    N = input()
    cnt = 0
    flag = False
    for i in N:
        if flag and (i == '0'):
            cnt += 1
            flag = False
        elif not flag and i == '1':
            cnt += 1
            flag = True
    print(f"#{tc} {cnt}")
T = int(input())

for tc in range(1, T + 1):
    N = list(map(int, input()))

    max_num = N[:]
    for i in range(len(max_num)):
        max_digit = max(max_num[i:])
        if max_digit > max_num[i]:
            # 뒤쪽에서 가장 오른쪽의 max_digit 찾기
            for j in range(len(max_num) - 1, i, -1):
                if max_num[j] == max_digit:
                    max_num[i], max_num[j] = max_num[j], max_num[i]
                    break
            break

    min_num = N[:]
    for i in range(len(min_num)):
        if i == 0:
            min_digit = min([x for x in min_num[i + 1:] if x != 0], default=min_num[i])
        else:
            min_digit = min(min_num[i:])

        if min_num[i] > min_digit:
            # 뒤쪽에서 가장 오른쪽의 min_digit 찾기
            for j in range(len(min_num) - 1, i, -1):
                if min_num[j] == min_digit:
                    min_num[i], min_num[j] = min_num[j], min_num[i]
                    break
            break

    max_val = ''.join(map(str, max_num))
    min_val = ''.join(map(str, min_num))

    print(f"#{tc} {min_val} {max_val}")
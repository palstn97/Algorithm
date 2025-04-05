N = int(input())
M = list(map(int, input().split()))
T, P = map(int, input().split())

M_cnt = 0
for i in M:
    if 0 < i <= T:
        M_cnt += 1
    elif i > T:
        if i % T == 0:
            M_cnt += (i // T)
        else:
            M_cnt += (i // T + 1)
    else:
        M_cnt += 0

P_group = N // P
P_one = N % P

print(M_cnt)
print(f"{P_group} {P_one}")
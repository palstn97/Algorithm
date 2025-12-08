H, M = map(int, input().split())
if M < 45:
    H = H - 1
    M = 15 + M
    if H < 0:
        H = 23
else:
    M = M - 45

print(str(H) + ' ' + str(M))
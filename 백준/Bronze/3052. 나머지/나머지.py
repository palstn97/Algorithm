S = [0] * 42
for i in range(10):
    num = int(input())
    res = num % 42
    S[res] += 1

cnt = 0
for j in range(len(S)):
    if S[j] != 0:
        cnt += 1

print(cnt)
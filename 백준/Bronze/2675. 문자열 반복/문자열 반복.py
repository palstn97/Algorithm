T = int(input())

for _ in range(T):
    R, S = map(str, input().split())
    res = ''
    for i in range(len(S)):
        for j in range(int(R)):
            res += S[i]

    print(res)
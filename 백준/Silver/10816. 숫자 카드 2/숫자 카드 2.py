N = int(input())
cards = list(map(int, input().split()))
M = int(input())
res = list(map(int, input().split()))

cnt = {}    # 딕셔너리로 찾기
for i in cards:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

lst = []
for j in res:
    if j in cnt:
        lst.append(cnt[j])
    else:
        lst.append(0)

print(*lst)
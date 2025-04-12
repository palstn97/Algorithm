N = int(input())
lst = []
for tc in range(N):
    W, H = map(int, input().split())
    lst.append((W, H))

for i in range(N):
    rank = 1    # 기본 순위로 1이라고 설정
    for j in range(N):
        if i == j:
            continue    # 동일인물이기 때문에 continue
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rank += 1   # 덩치가 작으면 순위 1 늘어나기
    print(rank, end=' ')

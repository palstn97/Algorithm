N = int(input())
parent = list(map(int, input().split()))
remove = int(input())

root = -1
for i in range(N):
    if parent[i] == -1:
        root = i
        break

children = [[] for _ in range(N)]
for i in range(N):
    p = parent[i]
    if p != -1:
        children[p].append(i)

def dfs(u):
    if u == remove:
        return 0
    cnt = 0
    leaf_children = 0
    
    for v in children[u]:
        if v == remove:
            continue
        cnt += 1
        leaf_children += dfs(v)

    if cnt == 0:
        return 1
    return leaf_children

if remove == root:
    print(0)
else:
    print(dfs(root))


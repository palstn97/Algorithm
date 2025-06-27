def DFS(x):
    visited = [False] * (N + 1)
    stack = [x] # DFS는 스택을 사용해서 시작 노드를 스택에 추가하는 방식으로 진행
    visited[x] = True
    cnt = 0
    while stack:    # stack이 채워져있으면
        node = stack.pop()  # 하나 추출 -> 현재 노드
        for next_node in graph[node]:   # 현재 노드에 연결된 모든 노드를 확인
            if not visited[next_node]:  # 방문처리가 안된 컴퓨터라면
                visited[next_node] = True   # 방문처리하고
                stack.append(next_node) # stack에 next_node 담아주기
                cnt += 1    # 바이러스에 걸린 컴퓨터이다.
    return cnt


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]  # 인접 리스트 방식으로 그래프 표현
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)  # 양방향 연결을 인접 리스트에 저장해주기
    graph[B].append(A)
print(DFS(1))
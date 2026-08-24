def dfs(graph, start, visited):
    visited[start] = True
    count = 1
    for next_node in graph[start]:
        if not visited[next_node]:
            count += dfs(graph, next_node, visited)
    return count

def solution(n, wires):
    answer = n + 1
    # dfs 사용하기
    for i in range(len(wires)):
        # wires에서 i번째 선만 빼고 그래프 구성하기
        graph = {j: [] for j in range(1, n + 1)}
        for idx, (v1, v2) in enumerate(wires):
            if idx != i:    # 끊을 전선은 빼고
                graph[v1].append(v2)
                graph[v2].append(v1)
                
        visited = [False] * (n + 1)
        cnt = dfs(graph, wires[i][0], visited)
        
        result = abs(cnt - (n - cnt))
        answer = min(answer, result)
    return answer
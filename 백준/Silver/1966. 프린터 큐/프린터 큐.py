'''
큐에 (우선순위, 인덱스) 이렇게 담아서 any() 함수 사용하여 우선순위가 더 작으면 뒤로 보내버린다.
현재보다 중요도가 높은 문서가 큐에 남아있는지 확인을 한다는 뜻이다. 
만약 그렇다면 큐의 뒷부분에 담아줄 것이고
그렇지 않다면 인쇄를 한다.
그리고 현재 인덱스가 내가 찾는 인덱스라면 인쇄 순서를 출력하고 break를 써서 탈출하자.
'''
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # (중요도, 원래 인덱스) 형태로 큐를 생성할거다
    q = deque((arr[i], i) for i in range(N))
    cnt = 0 # 인쇄 순서

    while q:
        current = q.popleft()

        # 현재보다 중요도가 높은 문서가 큐에 남아있는지 확인
        if any(current[0] < a[0] for a in q):
            q.append(current)
        else:
            cnt += 1    # 인쇄하기
            if current[1] == M:
                print(cnt)
                break
import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end_time = meetings[0][1]   # 정렬했으니까 0이면 가장 첫 번째 회의 끝나는 시간이 end_time으로 들어온다.

for i in range(1, N):   # 일단 0번째가 시작이니까 1부터 돌리기
    if meetings[i][0] >= end_time:
        cnt += 1
        end_time = meetings[i][1]

print(cnt)
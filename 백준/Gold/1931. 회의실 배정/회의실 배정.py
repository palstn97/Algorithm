N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간을 기준으로 정렬하고 만약 끝나는 시간이 같다면 시작 시간이 빠른 순으로 정렬하기 -> 튜플을 정렬할 때 첫 번재가 같으면 두 번째 요소를 비교한다.
# 이때 나는 lambda 함수를 써볼 것. -> lambda 매개변수: 반환값
meetings.sort(key=lambda x: (x[1], x[0]))
'''
일반 함수로 가면
def sort_key(x):
    return (x[1], x[0])

meetings.sort(key=get_sort_key)
'''

cnt = 1
end_time = meetings[0][1]   # 끝나는 시간을 가장 첫 번째 회의의 끝나는 시간으로 설정

for i in range(1, N):
    if meetings[i][0] >= end_time:  # 만약 시작시간이 끝나는 시간보다 크거나 같다면 다음 회의 진행 가능
        cnt += 1
        end_time = meetings[i][1]   # 끝나는 시간 재설정

print(cnt)
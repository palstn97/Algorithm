'''
최소힙을 사용하니 heapq를 import해보기
시작 시간을 기준으로 정렬하고 각 방의 종료 시간을 저장하는 리스트를 유지한다.
새 예약이 들어오면 모든 방을 확인해서 방의 종료시간 + 10분 <= 새 예약 시작시간 인 방이 있는지 체크하기
있으면 그 방에 배정하고 종료 시간 업데이트, 아니면 새로운 방 추가하기
'''

import heapq

def solution(book_time):
    # 시작 시간 기준으로 정렬
    times = []
    for start, end in book_time:
        start_time = int(start[:2]) * 60 + int(start[3:])
        end_time = int(end[:2]) * 60 + int(end[3:])
        times.append((start_time, end_time))
    times.sort()    # 시작 시간 순으로 정렬

    # 각 방의 종료 시간을 저장하기
    rooms = []  # 여기에서 최소힙을 사용한다? 어떻게??
    # 가장 빨리 끝나는 방이 사용가능한지 판단을 해주기!
    for start, end in times:
        if rooms and rooms[0] + 10 <= start:
            heapq.heappop(rooms)    # 가장 빨리 끝나는 방 제거

        heapq.heappush(rooms, end)
    
    return len(rooms)

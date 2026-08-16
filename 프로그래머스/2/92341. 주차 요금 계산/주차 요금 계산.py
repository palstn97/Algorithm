import math

def solution(fees, records):
    in_time = {}    # 입차한 차의 시간을 담아준다. 만약에 여기에 끝까지 남아있으면 23:59에 출차했다고 간주하기!
    total_time = {} # 총 시간을 담아주는 딕셔너리
    
    for record in records:
        time, car, action = record.split()  # 띄어쓰기를 기준으로 분리
        h, m = time.split(":")  # 시각과 분 분리
        time = int(h) * 60 + int(m)
        
        if action == "IN":
            in_time[car] = time
        else:
            total_time[car] = total_time.get(car, 0) + (time - in_time[car])
            del in_time[car]
            
    for car, t in in_time.items():
        total_time[car] = total_time.get(car, 0) + (1439 - t)  # 여전히 in_time에 남아있는 차량이 있다면 23:59에 출차했다고 간주하여 마저 계산하기
    
    # 요금 계산
    answer = []
    base_time, base_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    
    for car in sorted(total_time.keys()):
        m = total_time[car]
        if m <= base_time:
            fee = base_fee
        else:
            extra = m - base_time
            fee = base_fee + math.ceil(extra / unit_time) * unit_fee
        answer.append(fee)
        
    return answer
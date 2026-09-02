from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        counter = {}    # 각각의 조합을 담아줄 딕셔너리 생성
        for order in orders:
            order = sorted(order)   # 같은 메뉴 조합이라도 순서가 다르게 들어올 수 있기 때문에 처음부터 정렬을 하기
            for combo in combinations(order, c):
                counter[combo] = counter.get(combo, 0) + 1  # 처음 등장하는 조합이라면 get()이 0을 반환하고 1을 더해준다. 이미 있던 조합이라면 get()이 기존 값을 반환하고 거기에 1을 더해준다.
                
        if counter:
            max_count = max(counter.values())   # counter.values()는 딕셔너리의 값들만 모아서 보여줌
            if max_count >= 2:
                for combo, cnt in counter.items():
                    if cnt == max_count:
                        answer.append(''.join(combo))
            
    return sorted(answer)
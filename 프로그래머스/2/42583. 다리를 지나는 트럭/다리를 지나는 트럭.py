def solution(bridge_length, weight, truck_weights):
    answer = 0
    state = [0] * bridge_length # 다리 위 상태를 나타내는 리스트 -> 각 원소 해당 칸에 올라간 트럭의 무게
    while len(state) != 0:
        answer += 1
        state.pop(0)    # 트럭이 다리를 다 지난 상태
        if len(truck_weights) != 0: # 대기 중인 트럭이 있다면
            if sum(state) + truck_weights[0] <= weight: # 다리에 있는 트럭들 무게랑 새로 올릴 트럭의 무게 더한 값이 기준 무게보다 작거나 같다면
                state.append(truck_weights.pop(0))  # 트럭 새로 올리기
            else:
                state.append(0) # 그 외에는 빈칸으로 만들기 -> 트럭 못 올리기 때문에
                
    return answer   # 총 걸린 시간 return

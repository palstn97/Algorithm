def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = [0] * bridge_length
    while len(truck) != 0:
        answer += 1
        truck.pop(0)
        if len(truck_weights) != 0:
            if sum(truck) + truck_weights[0] <= weight:
                truck.append(truck_weights.pop(0))
            else:
                truck.append(0)
    return answer
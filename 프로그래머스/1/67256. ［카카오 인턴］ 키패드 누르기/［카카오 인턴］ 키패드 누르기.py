def solution(numbers, hand):
    pad = {
        1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2), '*':(3,0), 0: (3,1), '#': (3,2)
    }
    left = pad['*'] # 왼손의 위치
    right = pad['#']    # 오른손의 위치
    answer = ''
    
    for num in numbers:
        if num in (1, 4, 7):
            answer += 'L'
            left = pad[num]
        elif num in(3, 6, 9):
            answer += 'R'
            right = pad[num]
        else:   # 가로 + 세로 이동 칸수를 더한 방식으로 거리 측정하기
            left_len = abs(left[0] - pad[num][0]) + abs(left[1] - pad[num][1])
            right_len = abs(right[0] - pad[num][0]) + abs(right[1] - pad[num][1])
            if left_len < right_len:
                answer += 'L'
                left = pad[num]
            elif left_len > right_len:
                answer += 'R'
                right = pad[num]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = pad[num]
                else:
                    answer += 'L'
                    left = pad[num]
                    
    return answer
def solution(name, yearning, photo):
    n = len(name)
    point_dict = {}
    for i in range(n):
        point_dict[name[i]] = yearning[i]
        
    m = len(photo)
    answer = []
    
    for j in range(m):
        sum = 0
        for k in photo[j]:
            if k not in point_dict:
                sum += 0
            else:
                sum += point_dict[k]
        answer.append(sum)
    
    return answer
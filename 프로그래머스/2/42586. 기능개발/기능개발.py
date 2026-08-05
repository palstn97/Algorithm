import math

def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        extra = 100 - progresses[i]
        day = math.ceil((extra) / speeds[i])
        days.append(day)
    answer = []
    
    # 앞에서부터 순서대로 보면서 첫 번째 기능의 day가 그날의 배포 기준일이 된다.
    # 그 뒤의 기능들의 day가 앞의 day보다 작거나 같으면 같은 주기로 생각한다. 그렇지 않으면 주기를 초기화하고 새로 처음부터 다시 세어준다.
    standard = days[0]  # 배포 기준일로 설정
    deploy = 1
    for j in range(1, len(days)):
        if days[j] <= standard:
            deploy += 1
        else:
            answer.append(deploy)
            standard = days[j]
            deploy = 1
            
    answer.append(deploy)
    
    return answer
def solution(data, ext, val_ext, sort_by):
    col = {"code": 0, "date": 1, "maximum": 2, "remain": 3} # 항목의 이름을 저장한 딕셔너리! 그래야지만 ext와 sort_by를 정확하게 사용할 수 있다.
    
    answer = []
    for i in data:
        if i[col[ext]] < val_ext:   # 정답에 해당하는 것들 골라내서 answer에 담아주기
            answer.append(i)
            
    answer.sort(key=lambda x: x[col[sort_by]])  # x라는 매개변수를 하나 받는 함수를 만들고 x[col[sort_by]]를 반환하겠다!
    return answer
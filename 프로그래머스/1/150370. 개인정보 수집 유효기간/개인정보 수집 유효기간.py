def date(d):
    year, month, day = map(int, d.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    today_date = date(today)    # 현재 날짜
    
    term_dict = {}  # 유효기간 저장하는 딕셔너리
    for term in terms:
        term_type, duration = term.split()
        term_dict[term_type] = int(duration) * 28
        
    # 개인 정보 파기 여부
    answer = []
    for i, privacy in enumerate(privacies): # 인덱스도 같이 추출하기
        collect_date, collect_type = privacy.split()
        expire_date = date(collect_date) + term_dict[collect_type]
        if expire_date <= today_date:   # 파기해야할 정보 골라내기
            answer.append(i + 1)
    return answer
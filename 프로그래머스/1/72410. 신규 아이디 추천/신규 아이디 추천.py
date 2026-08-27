def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    allow = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    result = ''
    for i in new_id:
        if i in allow:
            result += i
    new_id = result
    # 3단계
    result = ''
    for i in new_id:
        if i == '.' and result and result[-1] == '.':
            continue    # 방금 넣은 것도 마침표면 건너뛰기(즉, continue로 중복 방지)
        result += i
    new_id = result
    # 4단계 -> .strip() -> 인자 없이 그냥 사용하면 양쪽 끝의 공백을 제거하는거고, 인자를 넣으면 원하는 문자를 지정해서 양쪽 끝에서 제거를 해준다.
    new_id = new_id.strip('.')
    # 5단계
    if not new_id:
        new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')  # 이렇게 해야지만 잘랐을 경우 마지막에 .이 있는 경우에 제거를 해줄 수 있다!
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    
    return new_id
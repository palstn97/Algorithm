from functools import cmp_to_key    # 두 값을 비교하는 함수를 sort()가 이해할 수 있는 형태로 바꿔줄 수 있다.

def compare(a, b):  # 어느 순서로 이어붙여야 더 큰 수가 되는지 판단하는 함수
    if a + b > b + a:
        return -1
    else:
        return 1

def solution(numbers):  # 숫자를 문자열로 반환
    strnum = list(map(str, numbers))    # numbers는 정수 리스트이기 때문에 문자열로 바꿔두는 것. map 객체를 사용해서 str()을 적용
    strnum.sort(key=cmp_to_key(compare))    # 매번 물어보면서 줄을 세우는, 즉 정렬을 하는 함수 사용!
    answer = ''.join(strnum)    # 문자열 원소를 구분자없이 하나로 이어붙이기
    if answer[0] == '0':    # 전부 0인 경우 0 반환
        return '0'
    return answer
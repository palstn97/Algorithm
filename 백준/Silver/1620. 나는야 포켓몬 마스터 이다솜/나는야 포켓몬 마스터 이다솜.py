# 숫자가 입력되면 해당 번호의 포켓몬 이름을 출력하고
# 이름이 입력되면 해당 포켓몬의 번호를 출력해야한다!
# 해시맵(딕셔너리) 2개 사용하는 방법이 가장 효율적..?

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 1. 번호 -> 이름을 찾는 딕셔너리 생성
num_to_name = {}
# 2. 이름 -> 번호를 찾는 딕셔너리 생성
name_to_num = {}
# 두개를 만드는 이유는 양방향 검색이 필요하기 때문! 하나만 있으면 한쪽 방향 검색이 느려진다.
for i in range(1, N + 1):
    name = input().rstrip()    # 포켓몬 이름을 입력받고 오른쪽 공백을 제거
    num_to_name[i] = name    # 딕셔너리에 번호 -> 이름 매핑을 저장
                             # 예를 들어 i=1, name = "피카츄"일 때 num_to_name[1] = "피카츄"
    name_to_num[name] = i    # 딕셔너리에 이름 -> 번호 매핑을 저장
                             # 예를 들어 name = "피카츄", i=1일 때 name_to_num["피카츄"] = 1

for _ in range(M):
    q = input().rstrip()    # 질문 입력 받고 공백을 제거
    if q.isdigit():  # 숫자인 경우 -> 문자열이 모두 숫자로 이루어져 있으면 True -> isdigit()를 쓴 이유는 숫자와 문자 입력을 구분하기 위해서이다!
        print(num_to_name[int(q)])
    else:   # 이름인 경우 -> 해당 포켓몬의 번호를  출력
        print(name_to_num[q])

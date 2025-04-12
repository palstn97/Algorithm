N = int(input())

end = 666
count = 1   # 1편이 666이니까 1부터 count하기

while True:
    if count == N:
        print(end)
        break
    end += 1    # 만약에 count가 N이 된다면 end를 출력하기
    if '666' in str(end):
        count += 1  # 만약 666이 포함되어 있다면 -> 이때 문자열에서 확인할 것 / count를 1 올려주기
        # 부르트포스 사용 -> 완전탐색
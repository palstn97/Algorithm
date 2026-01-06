K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

# 이분 탐색 사용할거니까, start의 값이랑 end의 값을 지정하고 mid를 구해야겠지?
# 근데 왜 이 문제가 이분 탐색인가?
# 그 이유는 반대 상황이 연출되기 때문이다. 즉 잘라야하는 길이가 길면 갯수가 적고 잘라야하는 길이가 짧으면 갯수가 늘어나기 때문에 서로 반대되는 상황이 나온다.
# 그렇기에 이분 탐색을 사용한다. 이분탐색은 start와 end를 설정하고 mid를 계속 설정하고 정답을 이 mid로 갱신을 하는거다. 그리고 while문을 사용할건데
# 종료가 되는 기준은 start가 end보다 커진다면 종료가 된다.
start = 1
end = max(cables)

result = 0  # 이게 내가 구해야하는 정답 -> mid로 계속 갱신

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for cable in cables:
        sum += (cable // mid)

    if sum >= N:    # 총합이 더 많다면?
        result = mid    # 일단 정답을 갱신해주고
        start = mid + 1 # 지금은 갯수가 많기 때문에 길이를 키워줘야하므로 start를 mid + 1로 설정하기
    else:
        end = mid - 1   # 갯수가 적기 때문에 길이를 줄여줘야지만 총합이 늘어나므로 end를 mid - 1로 설정하기

print(result)
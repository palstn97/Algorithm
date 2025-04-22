T = int(input())

for i in range(T):
    k = int(input())    # 층 수
    n = int(input())    # 호 수
    lst = [j for j in range(1, n + 1)]  # 0층의 사람들 리스트

    for k in range(1, k + 1):   # 1층부터 k층까지
        for l in range(1, n):
            lst[l] += lst[l - 1]    # l + 1호 사람 수 = 1호까지의 누적합으로 업데이트
            # 1층 -> [1, 3, 6, 10, 15 ... ] / 2층 -> [1, 4, 10, 20, 35 ... ] => 이전 층의 누적합
    print(lst[n - 1])   # k층의 n호 사람 수는 lst[n - 1]에 저장되어 있다.
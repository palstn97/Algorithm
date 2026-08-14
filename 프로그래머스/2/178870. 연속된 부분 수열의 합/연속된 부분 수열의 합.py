def solution(sequence, k):
    n = len(sequence)
    left = 0
    total = 0
    res = n + 1 # 갱신을 해주기 위한 것으로 전체 길이 + 1로 만들어 놓는다.
    answer = []
    
    for right in range(n):
        total += sequence[right]
        
        while total > k:    # 합이 k보다 크면 left 한 칸 땡기자.
            total -= sequence[left]
            left += 1
        if total == k:
            length = right - left + 1   # 현재 길이와 최적 길이 비교
            if length < res:
                res = length
                answer = [left, right]
            
    return answer
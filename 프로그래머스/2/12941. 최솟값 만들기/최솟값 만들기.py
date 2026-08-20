def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=False)
    
    for i in range(len(A)):
        mul = A[i] * B[i]
        answer += mul

    return answer
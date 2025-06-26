'''
현재 위치 기준 LCS는 이전 LCS에 +1을 더하거나 더하지 않거나 두 가지 중 한 가지를 선택
문자를 하나씩 증가시키면서 비교하기 -> 두 문자열을 2차원 행렬로 생각?
lcs[i][j]는 arr1의 처음부터 i번째 문자까지, arr2의 처음부터 j번째 문자까지 비교했을 때의 LCS를 뜻한다.
lcs[i][j] = lcs[i - 1][j - 1] + 1 -> 비교한 문자열이 같은 경우
lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j]) -> 비교한 문자열이 다른 경우
'''

arr1 = input()
arr2 = input()

lcs = [[0] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]   # dp를 사용하기 위한 2차원 리스트
# +1을 해주는 이유는 문자열의 인덱스를 1부터 시작해서 처리하면 i - 1, j - 1을 자유롭게 사용할 수 있다. lcs[0][j], lcs[i][0]은 공집합과 비교한 상태로 초기값이 0으로 설정된다.

# 문자열을 하나씩 비교하면서 LCS구하기
for i in range(1, len(arr1) + 1):
    for j in range(1, len(arr2) + 1):
        if arr1[i - 1] == arr2[j - 1]:  # 두 문자가 같다면
            lcs[i][j] = lcs[i - 1][j - 1] + 1   # 두 문자를 포함하지 않은 이전까지의 LCS 길이에 현재 같은 문자까지 더해준 것!
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])   # arr2에서 이전 문자까지 비교한 LCS와 arr1에서 이전 문자까지 비교한 LCS 중 큰 값을 선택

print(lcs[-1][-1])    # 가장 마지막 부분이 답
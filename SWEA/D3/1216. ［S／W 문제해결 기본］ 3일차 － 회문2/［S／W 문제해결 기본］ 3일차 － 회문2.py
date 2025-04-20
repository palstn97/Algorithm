def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


def palindrome(mat):
    for l in range(100, 0, -1): # 뒤에서부터 내려오면서 찾기
        for r in range(100):    # 가로 검사
            for c in range(100 - l + 1):
                word = mat[r][c:c + l]
                if is_palindrome(word):
                    return l
        # 세로 검사 -> 슬라이싱을 바로 사용할 수 없다. -> 열만 따로 슬라이싱 불가. 따라서 한칸 한칸 접근해서 수직으로 무자를 가져와야 한다.
        for c in range(100):
            for r in range(100 - l + 1):
                word2 = ''
                for i in range(l):
                    word2 += mat[r + i][c]
                if is_palindrome(word2):
                    return l
    return 0


for _ in range(10):
    tc = int(input())
    matrix = [list(input()) for _ in range(100)]
    print(f"#{tc} {palindrome(matrix)}")
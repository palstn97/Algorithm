import sys
sys.setrecursionlimit(10**6)

def postorder(start, end):
    if start > end: # 범위가 잘못되면 종료하기
        return
    # 첫 번째 값 = 루트
    root = preorder[start]

    # 오른쪽 서브트리 시작점 찾기(루트보다 큰 첫 번째 값)
    right_start = end + 1   # 없으면 끝 + 1
    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            right_start = i
            break

    # 왼쪽 서브트리 재귀
    postorder(start + 1, right_start - 1)
    # 오른쪽 서브트리 재귀
    postorder(right_start, end)
    # 루트 출력 -> 후위 순회는 루트가 마지막이니까
    print(root)

preorder = list(map(int, sys.stdin.read().split()))
postorder(0, len(preorder) - 1)
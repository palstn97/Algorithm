N = int(input())
# 리스트 말고 딕셔너리를 써서 바로 노드의 자식 정보에 접근 가능하도록 해보자. -> tree[node] = (left, right)

tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)

def preorder(node):
    if node == '.':
        return
    print(node, end='') # 루트 출력
    left, right = tree[node]    # 자식 정보 가져오기
    preorder(left)  # 왼쪽 자식 방문
    preorder(right) # 오른쪽 자식 방문

def inorder(node):
    if node == '.':
        return
    left, right = tree[node]
    inorder(left)
    print(node, end='')
    inorder(right)

def postorder(node):
    if node == '.':
        return
    left, right = tree[node]
    postorder(left)
    postorder(right)
    print(node, end='')

# 루트는 언제나 A
preorder('A')
print()
inorder('A')
print()
postorder('A')
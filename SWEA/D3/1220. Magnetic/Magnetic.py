# N극 자성체랑 S극 자성체 찾기
# 행이 아닌 열을 돌면서 세야한다. 왜냐면 N극과 S극이 각가 위 아래에 있기 때문이다.
# N극을 발견하면 S극이 있나 확인하기 위해서 S값에 True를 세팅하기 -> S극은 N극 자성체에 이끌려 사라지기 때문에 N극 발견 생각
# 교착 상태 발견하려면 우선 N극 자성체부터 발견해야 하고 S극을 발견할 시에 교착 상태가 발생한 것이므로 1개를 세고 다시 False로 세팅하기
def magnetic(mat):
    num = 0
    for c in range(100):    # 열 단위로 파악해야한다. -> 열부터 탐색
        found_N = False   # 매 열마다 초기화해주기 -> N극 자성체를 발견했는지 확인하는 용도
        for r in range(100):    # 각 열마다 위에서 아래로 순회하기
            if mat[r][c] == 1:  # N극 자성체면
                found_N = True    # S극이 올 때 교착이 되기 때문에 플래그를 True로 바꿔줄 것 -> S극을 기다릴 수 있도록 플래그 켜기
            if mat[r][c] == 2:  # S극 자성체면
                if found_N: # 만약 N극을 이전에 봤다면 교착 상태가 성립되기 때문에
                    num += 1    # 교착 상태로 1 증가하기
                    found_N = False # 교착 상태를 세어주었기 때문에 초기화하기
    return num


for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    print(f"#{tc} {magnetic(matrix)}")

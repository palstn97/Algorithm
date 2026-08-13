def solution(board, moves):
    basket = []
    answer = 0
    
    for move in moves:
        col = move - 1
        
        # 위에서부터 순회를 하면서 처음 만나는 인형을 찾아줄 것이다.
        for i in range(len(board)):
            if board[i][col] != 0:
                doll = board[i][col]
                board[i][col] = 0   # 인형 뽑았으니까 그 칸은 없어져야 한다.

                # basket 안에서 비교를 해야한다. 즉, basket에 뭐라도 있고, 현재의 doll이 basket의 가장 마지막 원소와 같다면 둘 다 제거하고 answer를 2를 올려준다.
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)
                break   # break를 해주지 않는다면 밑에 있는 것들을 계속해서 뽑게 된다.
    return answer
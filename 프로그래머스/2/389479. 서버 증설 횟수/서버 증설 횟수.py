def solution(players, m, k):
    result = 0
    server = [0] * 24

    for i in range(24):
        now_server = server[i]
        plus_server = players[i] // m
        if now_server < plus_server:
            new_server = plus_server - now_server
            if i + k < 24:
                for j in range(i, i + k):
                    server[j] += new_server
            else:
                for k in range(i, 24):
                    server[k] += new_server

            result += new_server

    return result
def solution(bandage, health, attacks):
    success = 0
    now_health = health
    max_health = health
    
    idx = 0
    for t in range(1, attacks[-1][0] + 1):
        if idx < len(attacks) and attacks[idx][0] == t:
            now_health -= attacks[idx][1]
            success = 0
            idx += 1
            if now_health <= 0:
                return -1
        else:
            success += 1
            now_health = min(now_health + bandage[1], max_health)
            if success == bandage[0]:
                success = 0
                now_health = min(now_health + bandage[2], max_health)
                    
    return now_health
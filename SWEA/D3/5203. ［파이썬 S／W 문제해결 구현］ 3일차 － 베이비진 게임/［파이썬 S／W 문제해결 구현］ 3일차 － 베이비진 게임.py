def check_run_triplet(cards):
    count = [0] * 10
    for card in cards:
        count[card] += 1

    for i in count:
        if i >= 3:
            return True

    for j in range(8):
        if count[j] and count[j + 1] and count[j + 2]:
            return True

    return False


def baby_gin_game(cards):
    player1_card = []
    player2_card = []

    for i in range(12):
        if i % 2 == 0:
            player1_card.append(cards[i])
            if len(player1_card) >= 3 and check_run_triplet(player1_card):
                return 1
        else:
            player2_card.append(cards[i])
            if len(player2_card) >= 3 and check_run_triplet(player2_card):
                return 2

    return 0


T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    print(f"#{tc} {baby_gin_game(arr)}")
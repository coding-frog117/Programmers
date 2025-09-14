def solution(players, callings):
    rank = {name: i for i, name in enumerate(players)}

    for call in callings:
        cur = rank[call]            
        front = cur - 1            
        front_player = players[front]

        players[front], players[cur] = players[cur], players[front]

        rank[call] -= 1
        rank[front_player] += 1

    return players
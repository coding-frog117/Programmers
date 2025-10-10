from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    dices = list(range(n))
    combi = combinations(dices, n//2)
    max_win = -1
    answer = []

    for a_dice in combi:
        b_dice = [i for i in dices if i not in a_dice]

        a_list = [dice[i] for i in a_dice]
        b_list = [dice[i] for i in b_dice]

        a_sums = [sum(x) for x in product(*a_list)]
        b_sums = [sum(x) for x in product(*b_list)]
        b_sums.sort()

        win = sum(bisect_left(b_sums, x) for x in a_sums)

        if win > max_win:
            max_win = win
            answer = [i+1 for i in a_dice] 

    return sorted(answer)
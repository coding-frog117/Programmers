from itertools import product
from itertools import combinations
from bisect import bisect_left

def solution(dice):
    dice_arr = [i for i in range(len(dice))]
    # a 주사위의 조합 구하기
    a_combi = combinations(dice_arr,len(dice)//2)
    max_dice = 0
    ans = -1

    # a주사위 조합별로 체크
    for idx,a_dice in enumerate(a_combi) :
        # a가 고른 주사위 제외하고 남은 주사위를 b가 가져감
        b_dice = list(set(dice_arr) - set(a_dice))
        
        a_list = []
        b_list = []
        for i in range(len(a_dice)):
            a_list.append(dice[a_dice[i]])
            b_list.append(dice[b_dice[i]])

        # a와 b의 모든 경우의 수 구함
        a_possible = list(product(*a_list))
        b_possible = list(product(*b_list))
        
        for idx,a in enumerate(a_possible) :
            a_possible[idx] = sum(a)
            b_possible[idx] = sum(b_possible[idx])
            
        # b가 가능한 수들의 조합보다 a가 몇개나 큰지 파악
        b_possible.sort()
        wins = sum(bisect_left(b_possible, num) for num in a_possible)
        if wins > max_dice :
            max_dice = wins
            ans = [i+1 for i in (list(a_dice))]
    return ans
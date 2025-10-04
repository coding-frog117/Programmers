from itertools import product
from itertools import combinations

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
        win = 0
        for i in range(len(a_dice)):
            a_list.append(dice[a_dice[i]])
            b_list.append(dice[b_dice[i]])

        # a와 b의 모든 경우의 구함
        a_possible = list(product(*a_list))
        b_possible = list(product(*b_list))

        possible = list(product(a_possible,b_possible))
        for a,b in possible:
            if sum(a) > sum(b):
                win += 1
        
        if win > max_dice :
            max_dice = win
            ans = [i+1 for i in (list(a_dice))]
    return ans
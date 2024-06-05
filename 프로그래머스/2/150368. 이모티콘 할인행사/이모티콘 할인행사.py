from itertools import product

def solution(users, emoticons):
    discount = [9,8,7,6]
    answer = []
    prices = [[] for i in range(len(emoticons))]
#     할인율별 모든 조합 구함
    for idx,emoticon in enumerate(emoticons):
        for dis in discount:
            prices[idx].append([(emoticon // 10 * dis),(10-dis)*10])
    combinations = list(product(*prices))
    combinationResult = [[0,0] for _ in range(len(combinations))]
    
#     유저별 계산
    for user in users:
        want = user[0]
        limit = user[1]
        for idx,combi in enumerate(combinations):
            getPrice = 0
            for price in combi:
                if price[1] >= want:
                    getPrice += price[0]
            if getPrice >= limit :
                combinationResult[idx][0] += 1
            else:
                combinationResult[idx][1] += getPrice
    combinationResult.sort(reverse=True)
    return combinationResult[0]
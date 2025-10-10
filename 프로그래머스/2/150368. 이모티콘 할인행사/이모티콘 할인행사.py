# 최대한 많은 이모티콘 플러스 가입 -> 이모티콘 구매 비용 최대
# 모든 이모티콘을 10,20,30,40퍼 별로 할인율 적용했을 때, 조합별 결과 모두 구해야함
from collections import defaultdict
from itertools import product

def solution(users, emoticons):
    percent = [10,20,30,40]
    discount = defaultdict(list)
    for emoticon in emoticons :
        for p in percent:
            discount[emoticon].append([int(emoticon - (emoticon*(p/100))),p])
    
    combinations = product(*discount.values())
    result = []
    
    for combi in combinations :
        emoticon_plus = 0
        total_price = 0
        for percent,limit in users:
            price = 0
            is_emoticon_plus = False
            for item_price,item_percent in combi:
                if item_percent >= percent:
                    price += item_price
                    if price >= limit:
                        is_emoticon_plus = True
                        emoticon_plus += 1
                        break
            if not is_emoticon_plus:
                total_price += price
                
        result.append([emoticon_plus,total_price])
    result.sort()
    return result[-1]
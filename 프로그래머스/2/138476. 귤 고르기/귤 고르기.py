def solution(k, tangerine):
    hashmap = {}
    for i in tangerine:
        if (hashmap.get(i)):
            hashmap[i] += 1
        else :
            hashmap[i] = 1
    
    arr = list(hashmap.values())
    arr.sort(reverse=True)
    
    answer = 0
    
    for i in arr:
        k -= i
        answer += 1
        if (k<=0):
            return answer
    
    return answer
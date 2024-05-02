from collections import deque

def findLRUCache(cache,reference):
    minsize = min(reference.values())
    minRefCache = []
    
    for i in cache:
        if reference[i] == minsize:
            minRefCache.append(i)
    return minRefCache[0]

def solution(cacheSize, cities):
    if cacheSize ==  0:
        return len(cities) * 5
    reference = {}
    answer = 0
    cache = deque()
    
    for city in cities:
        if city.lower() in cache:
            answer += 1
            cache.remove(city.lower())
            cache.insert(0,city.lower())
        
        else:
            if len(cache) == cacheSize:
                cache.pop()
            cache.insert(0,city.lower())
            answer += 5
            
    return answer
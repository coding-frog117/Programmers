import heapq

def solution(n, works):
    maxheap = []
    for i in works:  
        heapq.heappush(maxheap,-1*i)
    
    for i in range(n):
        target = heapq.heappop(maxheap)
        if target >= 0:
            return 0
        heapq.heappush(maxheap,target+1)
    
    ans = 0
    for i in maxheap:
        origin = -1*i
        ans += (origin**2)
    return ans
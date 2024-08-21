# window 크기를 k로 정하고 max 구하기, max중에서 가장 작은 값 구하기
import sys
import heapq
from collections import deque

def solution(stones, k):
    start = 0
    end = k
    heap = []
    arr = deque()
    for idx,i in enumerate(stones[start:end]):
        arr.append([i,idx])
        heapq.heappush(heap,[-i,idx])
    
    minmax = heap[0][0]*-1
    
    while end < len(stones):
        heapq.heappush(heap,[-stones[end],end])
        if heap[0][1] <= start:
            while heap[0][1] <= start:
                heapq.heappop(heap)
        
        minmax = min(minmax,-heap[0][0])
        start += 1
        end += 1
        
    return minmax    
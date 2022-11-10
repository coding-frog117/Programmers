import heapq
def solution(scoville, K):
    heap=[]
    count=0
    heapq.heapify(scoville)
    
    for count in range(1,len(scoville)):        
        num1=heapq.heappop(scoville)
        num2=heapq.heappop(scoville)
        newnum=num1+(num2*2)
        heapq.heappush(scoville,newnum)               
        if scoville[0]>=K:
            return count
    return -1
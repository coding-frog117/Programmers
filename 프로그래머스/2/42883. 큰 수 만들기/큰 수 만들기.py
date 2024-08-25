import heapq

def solution(number, k):
    answer = ''
    heap = []
    r = len(number)-k
    start = 0
    end = len(number)-r
    
    for idx,num in enumerate(number):
        heapq.heappush(heap,[-1*int(num),idx])
        if idx == end:
            pick = 0
            pick_idx = -1
            while pick_idx < start:
                i = heapq.heappop(heap)
                pick = i[0]
                pick_idx = i[1]
                
            answer += str(-1*pick)
            r -= 1
            start = pick_idx+1
            end = len(number)-r
            
    return answer
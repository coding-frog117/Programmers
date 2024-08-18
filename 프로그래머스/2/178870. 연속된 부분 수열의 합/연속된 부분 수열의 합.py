import sys

def solution(sequence, k):
    start =0
    end = 1
    if (sequence[start] == k):
        return [0,0]
    sum = sequence[start] + sequence[end]
    answer = [1,sys.maxsize]
    
    while start <= end:
        if start >= len(sequence) or end >= len(sequence):
            return answer
        if sum == k:
            currS , currE = answer
            if currE - currS > end-start :
                answer = [start,end]
            sum -= sequence[start]
            start += 1
            end += 1
            if end < len(sequence):
                sum += sequence[end]
            
        elif sum < k :
            end += 1
            if end < len(sequence):
                sum += sequence[end]
            
        elif sum > k :
            sum -= sequence[start]
            start += 1
        
    return answer
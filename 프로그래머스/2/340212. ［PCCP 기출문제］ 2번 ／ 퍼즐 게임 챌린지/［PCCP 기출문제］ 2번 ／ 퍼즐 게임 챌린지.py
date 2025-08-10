#1부터 100000까지 이진탐색

def solution(diffs, times, limit):
    answer = 0
    
    def isPossible(level):
        total = 0
        for idx,diff in enumerate(diffs):
            if diff <= level:
                total += times[idx]
                continue
            total += ((diff-level) * (times[idx-1]+times[idx])) + times[idx]
            if total > limit:
                return False
            
        if total > limit:
            return False
        return True
    
    first = 1
    last = max(diffs)
    mid = (last + first) // 2
    answer = last
    while True :
        if mid < 1 or mid > max(diffs):
            break
        # limit보다 작은 경우 last를 내림
        if isPossible(mid):
            answer = min(answer,mid)
            last = mid
        # limit보다 큰 경우 first를 올림
        else :
            first = mid
        if ((last + first) // 2 == mid) :
            break
        mid = (last + first) // 2
    return answer
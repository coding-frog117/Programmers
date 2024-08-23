# 파라메트릭 서치 : 결정 문제로 바꾸기 - n명의 인원이 다 건널 수 있는가?
# n명을 찾기 위해 이진탐색

def solution(stones, k):
    ans = -1
    def isPossible(mid,k):
        cnt = 0
        for i in stones:
            if i-mid <= 0:
                cnt+=1
            else:
                cnt = 0

            if cnt >= k:
                return False
        return True

    start = 0
    end = max(stones)
    mid = (start + end) // 2
    
    while start <= end:
        mid = (start + end) // 2
        if isPossible(mid,k):
            ans = max(ans,mid)
            start = mid+1
        else:
            end = mid-1
    return start

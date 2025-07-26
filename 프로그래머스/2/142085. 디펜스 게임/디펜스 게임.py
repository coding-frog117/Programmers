# enemy의 원소를 확인하면서 가장 작은 원소들의 합이 k보다 작거나 같은지 확인
# heapq를 활용... 처음 k개는 push만 하고 이후부터는 heap의 길이 - k 횟수만큼 pop한 것의 합 > n 이면 break
# 시도했는데 일부 시간 초과 남
# 현재값이 최댓값들의 최솟값보다 크다면 갱신

import heapq

def solution(n, k, enemy):
    total_sum = 0
    count = 0
    max_heap = []
    # 최댓값들의 합 (무적권 사용하는 애들)
    max_sum = 0
    necessary_count = len(enemy)-k
    
    for e in enemy :
        if count < k:
            total_sum += e
            max_sum += e
            heapq.heappush(max_heap,e)
            count += 1
            continue
        
        if max_heap[0] < e:
            top = heapq.heappop(max_heap)
            heapq.heappush(max_heap,e)
            max_sum = max_sum - top + e
        total_sum += e
        
        if total_sum - max_sum > n :
            return count
        count += 1
    return count
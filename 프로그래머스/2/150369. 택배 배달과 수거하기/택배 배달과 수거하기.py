# 아이디어 : 각 배열의 뒤에서부터 cap씩 빼준다. 더 큰 idx * 2만큼 answer에 더해줌
# 둘다 idx가 0이 되는 순간의 answer를 반환

def solution(cap, n, deliveries, pickups):
    d_idx = n-1
    p_idx = n-1
    d_sum = sum(deliveries)
    p_sum = sum(pickups)
    answer = 0
    
    while d_sum > 0 or p_sum >0:
        if d_idx > 0 :
            while deliveries[d_idx] <= 0:
                d_idx -= 1
                if d_idx < 0:
                    break
        if p_idx > 0:
            while pickups[p_idx] <= 0:
                p_idx -= 1
                if p_idx < 0:
                    break
            
        answer += (max(d_idx,p_idx)+1)*2
        cur_d_cap = cap
        cur_p_cap = cap
        while d_idx >= 0 and cur_d_cap > 0:
            if deliveries[d_idx] == 0:
                d_idx -= 1
                continue
            if deliveries[d_idx] >= cur_d_cap:
                deliveries[d_idx] = (deliveries[d_idx]-cur_d_cap)
                cur_d_cap = 0
            else:
                cur_d_cap -= deliveries[d_idx]
                deliveries[d_idx] = 0
                d_idx -= 1
                
        d_sum -= cap
            
        while p_idx >= 0 and cur_p_cap > 0:
            if pickups[p_idx] == 0:
                p_idx -= 1
                continue
            if pickups[p_idx] >= cur_p_cap:
                pickups[p_idx] = (pickups[p_idx]-cur_p_cap)
                cur_p_cap = 0
            else:
                cur_p_cap -= pickups[p_idx]
                pickups[p_idx]= 0
                p_idx -= 1
        p_sum -= cap
    return answer
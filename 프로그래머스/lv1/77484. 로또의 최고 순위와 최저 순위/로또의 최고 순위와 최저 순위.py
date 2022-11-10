def solution(lottos, win_nums):
    
    count=0
    zero_count=0
    for i in lottos:
        if i==0:
            zero_count+=1
        else:            
            for j in win_nums:
                if i==j:
                    count+=1
    bestcase=count+zero_count
    worstcase=count    
                
    if bestcase==0:
        bestcase=6
    elif 0<bestcase<7:
        bestcase=7-bestcase
        
    if worstcase==0:
        worstcase=6
    elif 0<worstcase<7:
        worstcase=7-worstcase
    
    return [bestcase,worstcase]
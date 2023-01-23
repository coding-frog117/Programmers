def solution(citations):
    answer = 0
    newarr= sorted(citations, reverse=True)
    
    for i in range(len(citations)):
        if newarr[i] <= i+1 :
            if newarr[i] == i+1:
                answer = newarr[i]
            else:
                answer = i
            break
            
    if newarr[-1] > len(citations):
        answer = len(citations)
        
    return answer
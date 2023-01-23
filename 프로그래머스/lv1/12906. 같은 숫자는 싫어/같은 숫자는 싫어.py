def solution(arr):
    answer = [arr[0]]
    prevnum = arr[0]
    
    if len(arr) == 1:
        return arr
    
    for i in arr:
        if prevnum == i:
            pass
        else:
            answer.append(i)
            prevnum=i
        
    return answer
def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(total,index):
        global answer
        if (index==len(numbers)-1):
            if (total == target):
                answer+=1
                
            return
        
        else :
            dfs(total+numbers[index+1],index+1)
            dfs(total-numbers[index+1],index+1)
    
    dfs(numbers[0],0)
    dfs(-numbers[0],0)
    
    return answer
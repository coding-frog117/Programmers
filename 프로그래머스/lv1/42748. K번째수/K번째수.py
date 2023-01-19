def solution(array, commands):
    answer=[]
    for command in commands:
        newarr= array[command[0]-1 : command[1]]
        newarr.sort()
        answer.append(newarr[command[2]-1])
        
    return answer
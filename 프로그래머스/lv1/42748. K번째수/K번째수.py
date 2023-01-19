def solution(array, commands):
    answer=[]
    length=len(commands)
    for i in range(length):
        data=array[commands[i][0]-1:commands[i][1]]
        data.sort()
        num=commands[i][2]-1
        answer.append(data[num])
        
    return answer
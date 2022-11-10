def solution(progresses, speeds):
    answer = []
    stack=[]
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]==0:
            stack.append((100-progresses[i])//speeds[i])
        else:
            stack.append((100-progresses[i])//speeds[i]+1)
    first=stack[0]
    count=0
    for i in stack:
        if first>=i:
            count=count+1
            
        else:
            answer.append(count)
            first=i
            count=1
            
    answer.append(count)
    return answer
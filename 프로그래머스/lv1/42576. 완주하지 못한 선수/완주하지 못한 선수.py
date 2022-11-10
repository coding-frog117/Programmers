def solution(participant, completion):
    table={}
    for i in participant:
        person=table.get(i)
        if person is None:
            table[i]=0
        table[i]+=1
    
    for j in completion:
        table[j]-=1
        
    for i in table:
        if table[i]!=0:
             answer = i
                
    return answer
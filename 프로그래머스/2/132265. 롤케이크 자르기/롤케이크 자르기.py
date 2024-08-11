# 중복 확인 위해 set에 보관, 각 케이크를 양쪽에서 이동하면서 종류 확인

def solution(topping):
    if len(topping) == 1:
        return 0
    front = {}
    back = {}
    answer = 0
    
    for i in topping:
        if back.get(i) == None:
            back[i] = 1
        else:
            back[i] += 1
        
    for i in topping:
        if front.get(i) == None:
            front[i] = 1
        else:
            front[i] += 1
        
        if back.get(i) == 1:
            back.pop(i)
        else:
            back[i] -= 1
        
        if len(front) == len(back):
            answer += 1
    
    return answer
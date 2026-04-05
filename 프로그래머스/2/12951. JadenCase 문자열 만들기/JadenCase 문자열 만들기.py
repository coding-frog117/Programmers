def solution(s):
    answer = ''
    isFirst = True
    
    for i in s:
        if i == " ":
            isFirst = True
            answer += " "
            continue
        if isFirst :
            answer += i.upper()
            isFirst = False
        else :
            answer += i.lower()      
    return answer
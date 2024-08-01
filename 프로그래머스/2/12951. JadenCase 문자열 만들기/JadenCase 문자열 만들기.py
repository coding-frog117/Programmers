def solution(s):
    answer = ''
    curr = ''
    
    for i in s:
        if i == ' ':
            answer += ' '
            curr = ''
        elif curr == '' :
            answer += i.upper()
            curr += i
        else :
            answer += i.lower()
    return answer
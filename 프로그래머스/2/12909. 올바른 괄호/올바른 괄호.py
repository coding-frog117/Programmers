def solution(s):
    stack = []
    if len(s) == 1 :
        return False
    
    for i in s:
        if i == '(':
            stack.append(i)
        else :
            if len(stack) >= 1 and stack[-1] == '(':
                stack.pop()
            else :
                return False
    if stack :
        return False
    else:
        return True
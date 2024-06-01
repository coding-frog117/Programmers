def splitStr(p):
    u = ''
    v = ''
    open_count =0
    close_count = 0
    for idx,val in enumerate(p) :
        if val == '(':
            open_count += 1
        else :
            close_count += 1
        u += val
        if open_count == close_count:
            if idx < len(p):
                v = p[idx+1:]
            break
    return u,v

def isValid(string):
    stack =[]
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
    if stack :
        return False
    return True
        
def reverseStr(string):
    newStr = ''
    for i in string:
        if i == '(':
            newStr += ')'
        else:
            newStr += "("
    return newStr
    
def solution(p):
    # 1
    if p == '':
        return p
    # 2
    u,v = splitStr(p)
    # 3
    if isValid(u):
        u += solution(v)
        return u
    else:
        newStr = '(' + solution(v) + ')'
        u = u[1:len(u)-1]
        reversedStr = reverseStr(u)
        newStr += reversedStr
        return newStr
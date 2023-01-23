def solution(s):
    arr=[]
    prev=s[0]
    
    for i in s:
        if i == '(':
            arr.append('(')
            prev= '('
        else:
            if arr == []:
                return False
            else:
                if prev == '(':
                    arr.pop()
        
    if arr == []:
        return True
    else:
        return False
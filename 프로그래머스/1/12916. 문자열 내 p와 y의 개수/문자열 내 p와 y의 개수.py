def solution(s):
    p =0
    y = 0

    for i in s:
        if i.lower() == 'p':
            p+=1
        elif i.lower() == 'y':
            y += 1
    if p == y:
        return True
    return False
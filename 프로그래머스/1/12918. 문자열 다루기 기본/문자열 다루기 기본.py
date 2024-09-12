def solution(s):
    if (len(s) == 4 or len(s) == 6):
        for i in s:
            if i.isdigit() == False:
                return False
    else:
        return False
    return True
def solution(angle):
    if 0<angle and 90>angle:
        answer=1
    elif angle==90:
        answer=2
    elif 90<angle and angle<180:
        answer=3;
    else:
        answer=4
    return answer
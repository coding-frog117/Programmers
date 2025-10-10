from collections import defaultdict
# 각 점수를 4로 나눈 나머지를 각 유형별 점수에 더해줌

def solution(survey, choices):
    standard = [["R","T"],["C","F"],["J","M"],["A","N"]]
    scores = defaultdict(int)
    answer = ""
    
    for idx,s in enumerate(survey):
        first,second = s
        if choices[idx] < 4 :
            scores[first] += (4 - choices[idx])
        else:
            scores[second] += (choices[idx] - 4)
    
    for first,second in standard:
        if scores[first] >= scores[second] :
            answer += first
        else :
            answer += second
    return answer
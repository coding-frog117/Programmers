# 일단 역으로 정렬해서 각 상자 최저 사과점수 다 더한 다음에 m 곱해주기

def solution(k, m, score):
    score.sort(reverse=True)
    minScore=0
    
    for i in range(m-1,len(score),++m):
        minScore+=score[i]
        
    answer=minScore*m
    return answer
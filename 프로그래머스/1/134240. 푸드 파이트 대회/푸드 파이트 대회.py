def solution(food):
    answer = ''
    for i in range(1,len(food)):
        cnt = food[i] // 2
        answer += str(i) * cnt
        
    reverse = answer[::-1]
    answer += '0'
    answer += reverse
    return answer
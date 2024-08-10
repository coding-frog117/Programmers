def solution(s):
    s = s.split(' ')
    s = list(map(int,s))
#     값 정렬
    s.sort()
    answer = f'{s[0]} {s[-1]}'
    return answer
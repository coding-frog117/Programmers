from collections import defaultdict

def solution(name, yearning, photo):
    answer = [0 for i in range(len(photo))]
    dic = defaultdict(int)
    for idx,i in enumerate(name):
        dic[i] = yearning[idx]
    
    for idx,i in enumerate(photo) :
        for name in i:
            answer[idx] += dic[name]
    return answer
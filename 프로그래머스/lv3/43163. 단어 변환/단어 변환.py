from collections import deque

def solution(begin, target, words):
    
    if (target not in words):
        return 0
    
    queue = deque()
    queue.append((begin,0))
    
    while queue:  
        changeString,step = queue.popleft()
            
        if (changeString == target):
            return step
            
        for word in words:
            if (changeString == word):
                pass;
            
            count = 0
            for i in range(len(word)):
                
                if (changeString[i] == word[i]):
                    count += 1
                else :
                    newString = list(changeString)
                    newString[i] = word[i]
                    newString = ''.join(newString)
            
            if (count == len(word)-1):
                queue.append((newString,step+1))
                
#                 기존에 word를 자리마다 돌면서 하나씩 다 바꿔가며 존재하는 단어를 모두 탐색함.(테케 3번 시간초과) -> 자릿수가 하나만 다른 word를 모두 탐색함.
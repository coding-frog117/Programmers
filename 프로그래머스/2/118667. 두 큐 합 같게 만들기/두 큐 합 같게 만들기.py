# 해결 전략 : 각 큐에서 합이더 작은 큐가 더 큰 큐로 이동시키기
# 하나의 큐 합만 따지면 됨
# 각 큐가 처음 반대 큐와 상태가 같아지면 -1
from collections import deque

def solution(queue1, queue2):
    halfSum = (sum(queue1) +sum(queue2)) // 2
    if max(queue1) > halfSum or max(queue2) > halfSum:
        return -1
     
    q1_endIdx = len(queue1) -1
    q2_endIdx = len(queue2) -1
    for i in range(len(queue1)*3):
        queue1.append(0)
        queue2.append(0)
   
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    queue1Sum = sum(queue1)
    
    while True:
        if halfSum == queue1Sum:
            return answer
        elif halfSum > queue1Sum:
            if not queue2:
                return -1
            num = queue2.popleft()
            if num == 0:
                return -1
            
            q1_endIdx += 1
            q2_endIdx -= 1
            
            if q1_endIdx >= len(queue1):
                return -1
            queue1[q1_endIdx] = num
            queue1Sum += num
            answer += 1
        elif halfSum < queue1Sum:
            if not queue1:
                return -1
            num = queue1.popleft()
            if num == 0:
                return -1
            
            queue1Sum -= num
            q1_endIdx -= 1
            q2_endIdx += 1
            if q2_endIdx >= len(queue2):
                return -1
            queue2[q2_endIdx] = num
            answer += 1
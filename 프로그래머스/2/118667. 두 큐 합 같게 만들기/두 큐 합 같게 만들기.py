# 큰 쪽에서 작은 쪽으로 옮기면서 완전탐색?
from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1 = sum(queue1)
    q2 = sum(queue2)
    count = 0
    init_len = len(queue1)
    
    while q1 != q2 and count <= init_len*2+init_len-1:
        if q1 > q2 :
            num = queue1.popleft()
            queue2.append(num)
            q1 -= num
            q2 += num
        else :
            num = queue2.popleft()
            queue1.append(num)
            q2 -= num
            q1 += num
        count += 1
    if count > init_len*2+init_len-1:
        return -1
    return count
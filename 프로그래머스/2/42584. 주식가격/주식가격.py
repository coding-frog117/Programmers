# stack에 [price,idx]쌍을 저장
# stack의 top보다 크면 push, 작으면 pop하고 idx의 차이를 저장

def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    for idx,price in enumerate(prices):
        if not stack:
            stack.append([price,idx])
            continue
        if stack[-1][0] > price:
            while stack[-1][0] > price:
                cur_price,cur_idx = stack.pop()
                answer[cur_idx] = idx-cur_idx
                if not stack:
                    break
        stack.append([price,idx])
    
    if stack:
        for cur in stack:
            cur_price,cur_idx = cur
            answer[cur_idx] = len(prices)-1-cur_idx
    return answer
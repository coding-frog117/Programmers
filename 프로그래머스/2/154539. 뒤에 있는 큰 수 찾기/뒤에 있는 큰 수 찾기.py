# 오른쪽부터 이동하면서 현재 스택의 top보다 크면 pop, 작으면 push

def solution(numbers):
    answer = []
    stack = []
    
    for i in range(len(numbers)-1,-1,-1):
        if not stack:
            stack.append(numbers[i])
            answer.append(-1)
        elif stack[-1] <= numbers[i]:
            all_pop = False
            while stack[-1] <= numbers[i]:
                stack.pop()
                if not stack:
                    stack.append(numbers[i])
                    answer.append(-1)
                    all_pop = True
                    break
            if all_pop:
                continue
            answer.append(stack[-1])
            stack.append(numbers[i])
            
        elif stack[-1] > numbers[i]:
            answer.append(stack[-1])
            stack.append(numbers[i])
    return list(reversed(answer))
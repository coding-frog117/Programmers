# deque을 밀면서 현재 무게 + 다음 트럭이 limit보다 작거나 같고, deque의 마지막이 null이면 다음 트럭 push

from collections import deque

def solution(bridge_length, weight, truck_weights):
    initial = [None]*bridge_length
    queue = deque(initial)
    trucks = deque(truck_weights)
    time = 0
    curr_sum = 0
    
    while queue or trucks:
        time += 1
        curr = queue.popleft()
        if curr != None :
            curr_sum -= curr
        if not trucks:
            continue

        if curr_sum + trucks[0] <= weight and len(queue) < bridge_length:
            new_trucks = trucks.popleft()
            queue.append(new_trucks)
            curr_sum += new_trucks
        else:
            queue.append(None)
    return time
    
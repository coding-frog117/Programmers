def solution(n, wires):
    # countArray = [0 for i in range(n+1)]
    
    if (n==2):
        return 0;
    
    if (n==3):
        return 1;
    
    answer = []
    
    for i in range(len(wires)):
        seen =[];
        stack = [];
        
#       모든 index를 돌면서 해당 index가 제거된 새로운 배열 생성
        newWires = wires[0:i] + wires[i+1:]
        
        stack.append(newWires[0]);
        seen.append(newWires[0]);
        
#       새로운 배열에 대한 dfs
        while stack:
            item = stack.pop()
            
            for wire in newWires:
                if (wire in seen):
                    continue;
                if (item[0] in wire or item[1] in wire):
                    
                    stack.append(wire)
                    seen.append(wire)
    
        # print(i,seen)
        firstConnect = len(seen) +1
        secondConnect = n - firstConnect
    
        answer.append(abs(firstConnect-secondConnect))
        
    return min(answer)
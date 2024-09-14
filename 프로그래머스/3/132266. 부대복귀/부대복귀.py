from collections import deque
import sys
import copy

def solution(n, roads, sources, destination):
    maps = [[] for i in range(n+1)]
    min_cost = [sys.maxsize]*(n+1)
    ans = []
    
    for road in roads:
        x,y = road
        maps[x].append(y)
        maps[y].append(x)
        
    def BFS(source):
        length = 0
        queue = deque()
        seen = [False]*(n+1)
        seen[source] = True
        min_cost[source] = 0
        queue.append([source,0])
        
        while queue:
            cur_node,cnt = queue.popleft()
            
            for node in maps[cur_node]:
                if seen[node] == False:
                    seen[node] = True
                    min_cost[node] = cnt+1
                    queue.append([node,cnt+1])
    
    BFS(destination)
    for source in sources:
        if min_cost[source] == sys.maxsize :
            ans.append(-1)
        else:
            ans.append(min_cost[source])
    
    return ans
            
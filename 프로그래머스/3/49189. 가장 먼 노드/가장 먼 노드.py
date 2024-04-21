from collections import deque

def solution(n, edge):
    adj_array=[[] for _ in range(n+1)]
    for (a,b) in edge:
        adj_array[a-1].append(b-1)
        adj_array[b-1].append(a-1)
            
    length_count=[0 for _ in range(n)]    
    q=deque()
    
    seen=set()
    q.append(0)
    seen.add(0)
    
    while q:
        num=q.popleft()
        adjs=adj_array[num]
        for adj in adjs:
            if adj not in seen:
                seen.add(adj)
                q.append(adj)
                length_count[adj]=length_count[num]+1
    length_count.sort(reverse=True)
    answer=length_count.count(length_count[0])
       
    return answer
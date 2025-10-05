from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    nodes = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    # 간선 정보 저장
    for a, b in edges:
        nodes[a].append(b)
        in_degree[b] += 1
        out_degree[a] += 1
    
    # 생성 정점 찾기
    for node in out_degree:
        if out_degree[node] >= 2 and in_degree[node] == 0:
            answer[0] = node
            break
    
    seen = set()
    
    def DFS(start):
        cur = start
        visited = set()
        has_split = False
        
        while True:
            visited.add(cur)
            if out_degree[cur] == 0:
                # 막대 그래프
                answer[2] += 1
                return visited
            
            if out_degree[cur] >= 2:
                has_split = True
            
            nxt = nodes[cur][0]
            if nxt in visited:
                # 사이클 발견
                if has_split:
                    answer[3] += 1
                else:
                    answer[1] += 1
                return visited
            
            cur = nxt
    
    for nxt in nodes[answer[0]]:
        if nxt not in seen:
            part_seen = DFS(nxt)
            seen.update(part_seen)
    
    return answer
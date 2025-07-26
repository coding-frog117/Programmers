# A배열의 합, B배열의 합 구한후 완전탐색?
# 조합 구해서 모든 케이스 체크
# 시간 초과남 ...
# 조합의 갯수가 많은 것부터 체크해서 A_min이 갱신되었다면 얼리 리턴해주도록 수정

# 그래도 안풀림. DFS로 풀어야 하는것 같아서 수정


def solution(info, n, m):
    answer = 99999
    
    seen = set()
    stack = []
    stack.append([0,0,-1])
    while stack:
        a,b,i = stack.pop()
        if (a,b,i) in seen :
            continue
            
        if a >= n or b >= m :
            continue
            
        if i >= (len(info) - 1):
            answer = min(a,answer)
            continue
            
        stack.append([a+info[i][0],b,i+1])
        stack.append([a,b+info[i][1],i+1])
        
        seen.add((a,b,i))
    if answer >= n :
        return -1
    return answer
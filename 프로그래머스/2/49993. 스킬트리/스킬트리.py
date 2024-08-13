# 각 스킬에 해당하는 해시값 지정(초기값 false) 
# 스킬트리를 돌면서 해당하는 값이 있고, 이전에 false값이 나타났는지 확인

def solution(skill, skill_trees):
    answer = 0
    
    for cur_skill in skill_trees:
        skill_map = {}
        for i in skill:
            skill_map[i] = False
        sequential = True
        
        for s in cur_skill:
            if skill_map.get(s)==None:
                continue
            for j in skill:
                if j == s and sequential:
                    skill_map[s] = True
                    break
                elif skill_map[j] == False:
                    sequential = False
        if sequential:
            answer+= 1
    return answer
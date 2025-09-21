# 문자열로 각 케이스를 관리
# -인 키는 모든 경우를 합친것
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = {}
    lang = {"cpp": "0", "java": "1", "python": "2"}
    category = {"backend": "0", "frontend": "1"}
    level = {"junior": "0", "senior": "1"}
    prefer = {"chicken": "0", "pizza": "1"}
    
    # info 데이터 저장
    for i in info:
        i_lang, i_category, i_level, i_prefer, i_score = i.split()
        key = lang[i_lang] + category[i_category] + level[i_level] + prefer[i_prefer]
        if key not in dic:
            dic[key] = []
        dic[key].append(int(i_score))
    
    # 각 key마다 점수 정렬 (한 번만)
    for k in dic:
        dic[k].sort()
        
    # query 처리
    for q in query:
        q_lang, q_category, q_level, q_prefer_score = q.split(" and ")
        q_prefer, q_score = q_prefer_score.split()
        q_score = int(q_score)
        
        # 각 조건에 맞는 후보 key 조합 만들기
        if q_lang == "-":
            q_lang = lang.values()
        else:
            q_lang = [lang[q_lang]]
            
        if q_category == "-":
            q_category = category.values()
        else:
            q_category = [category[q_category]]
        
        if q_level == "-":
            q_level = level.values()
        else:
            q_level = [level[q_level]]
            
        if q_prefer == "-":
            q_prefer = prefer.values()
        else:
            q_prefer = [prefer[q_prefer]]
        
        # 후보 key들에 대해 점수 이진 탐색
        cnt = 0
        for l in q_lang:
            for c in q_category:
                for le in q_level:
                    for p in q_prefer:
                        key = l + c + le + p
                        if key in dic:
                            scores = dic[key]
                            idx = bisect_left(scores, q_score)
                            cnt += len(scores) - idx
        answer.append(cnt)
    
    return answer
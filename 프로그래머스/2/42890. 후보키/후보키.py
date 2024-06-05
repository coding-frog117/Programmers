from itertools import combinations
# 조합 중에서 같은 내용이 없는 조합 고르기
# 조합에서 하나의 속성을 뺀 것이 이미 후보키라면 제외하기(예를 들어 학번이 후보키라면 학번을 포함한 조합은 모두 제외)

def solution(relation):
    answer = []
    # 각 갯수별 조합 생성
    attributeIdx = [i for i in range(len(relation[0]))]
    for i in range(1,len(relation[0])+1):
        combi = list(combinations(attributeIdx,i))
        # 조합의 인덱스에 맞게 새로운 배열 생성
        arr = [[] for _ in range(len(combi))]
        for combi_idx,com in enumerate(combi) :
            for relation_idx,item in enumerate(relation):
                arr[combi_idx].append([])
                for i in com:
                    arr[combi_idx][relation_idx].append(item[i])
            # set으로 변환시켜 relation의 길이와 같은 조합만 추가(중복 없는 것 고르기)
            arr[combi_idx] = set(list(map(tuple,arr[combi_idx])))
            
            # 조합에서 하나의 속성을 뺀 것이 이미 후보키라면 제외하기(예를 들어 학번이 후보키라면 학번을 포함한 조합은 모두 제외
            if len(arr[combi_idx]) == len(relation) :
                isPossible = True
                if not answer:
                    answer.append(com)
                else:
                    for i in answer:
                        if len(set(i+com)) <= len(com):
                            isPossible = False
                    if isPossible :
                        answer.append(com)
                
    return len(answer)
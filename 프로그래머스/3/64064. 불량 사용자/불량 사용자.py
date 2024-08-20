from itertools import permutations

def isPossible(curr,ban):
    if len(curr) != len(ban):
        return False
    for i in range(len(ban)):
        if ban[i] !='*' and curr[i] != ban[i]:
            return False
    else:
        return True
    
def solution(user_id, banned_id):
    ans_set = set()
    permu_id = list(permutations(user_id,len(banned_id)))
    banned_id.sort(key = lambda x:len(x))
    
    for combi in permu_id:
        combi = list(combi)
        combi.sort(key = lambda x:len(x))
        for i in range(len(banned_id)):
            if not isPossible(combi[i],banned_id[i]):
                break
        else:
            combi.sort()
            ans_set.add(tuple(combi))
    return len(ans_set)
from itertools import product

def solution(user_id, banned_id):
    ans_set = []
    for ban in banned_id:
        participants = []
        for user in user_id:
            if len(user) != len(ban):
                continue
            for i in range(len(ban)):
                if ban[i] !='*' and user[i] != ban[i]:
                    break
            else:
                participants.append(user)
        ans_set.append(participants)
    products = list(product(*ans_set))
    ans = set()
    
    for i in products:
        if len(set(i)) == len(banned_id) :
            ans.add("".join(sorted(set(i))))
    return len(ans)
        
def solution(d, budget):
    count=0
    d.sort()
    for i in d:
        budget-=i
        if budget<0:
            return count
        count+=1
    return count
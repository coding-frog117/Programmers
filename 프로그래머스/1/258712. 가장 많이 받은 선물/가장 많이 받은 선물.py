def solution(friends, gifts):
    present = [[0]*len(friends) for _ in range(len(friends))]
    
    names = {}
    getPresent = [0 for _ in range(len(friends))]
    presentScore = [0 for _ in range(len(friends))]
    
    for i in range(len(friends)):
        if (names.get(friends[i]) == None):
            names[friends[i]] = i
    
    for gift in gifts:
        name = gift.split(' ')
        name1 = name[0]
        name2 = name[1]
    
        present[names[name1]][names[name2]] += 1
        presentScore[names[name1]] += 1
        presentScore[names[name2]] -= 1
   
    for i in range(len(present)) :
        for j in range(i+1,len(present)):
            if (present[i][j] > present[j][i]) :
                getPresent[i] += 1
            elif (present[i][j] < present[j][i]):
                getPresent[j] += 1
            else : 
                if (presentScore[i] > presentScore[j]):
                    getPresent[i] += 1
                elif (presentScore[i] < presentScore[j]):
                    getPresent[j] += 1
                else :
                    continue
                   
    answer = max(getPresent)
    return answer
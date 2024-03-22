def solution(word):
    initialState = [-1,-1,-1,-1,-1]
    wordDict = {'A':0,'E':1,'I':2,'O':3,'U':4} 
    
    global count
    count = 0
    word = list(word)
    
    for i in range(len(word)):
        word[i] = wordDict.get(word[i])
        
    while (len(word) < 5):
        word.append(-1)
        
    def floorUp(index):
            if (index == -6):
                return;
            
            if (initialState[index]) == 4:
                initialState[index] = -1;
                floorUp(index-1)
            else :
                initialState[index] += 1
                
    while True: 
        if (initialState == word or initialState == [4,4,4,4,4]):
            return count
            break
            
        if (-1 in initialState) :
            for i in range(len(initialState)):
                if (initialState[i] == -1):
                    initialState[i] =0 
                    count += 1
                    break;
            continue
            
        if (initialState[-1]) == 4:
            floorUp(-1)
        else :
            initialState[-1] += 1
        count += 1
    
    return count
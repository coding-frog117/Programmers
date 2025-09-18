def solution(new_id):
    word = new_id.lower()
    new_word = ""
    for w in word:
        if w.islower() or w.isdigit() or w in ["-","_","."]:
            new_word += w
            
    while ".." in new_word:
        new_word = new_word.replace("..",".")
        
    new_word2 = ""
    for idx,w in enumerate(new_word):
        if (idx == 0 or idx == len(new_word)-1) and w == ".":
            continue
        new_word2 += w
    
    if new_word2 == "":
        new_word2 += "a"
        
    if len(new_word2) >= 16:
        new_word2 = new_word2[:15]
        if new_word2[-1] == ".":
            new_word2 = new_word2[:14]
            
    if len(new_word2) <= 2:
        while len(new_word2) < 3:
            new_word2 += new_word2[-1]
            
    return new_word2
def checkPalindrome(S,s,e,max_len):
    while s < e:
        if S[s] != S[e]:
            return False
        s += 1
        e -= 1
    
    return True

def solution(S):
    max_len = -1
    s = 0
    
    while s < len(S):
        for i in range(len(S)-1,s,-1):
            e = i
            if e-s+1 <= max_len:
                break
            if checkPalindrome(S,s,e,max_len) != False:
                max_len = max(max_len,e-s+1)
        s += 1
    
    if max_len == -1:
        return 1
    return max_len
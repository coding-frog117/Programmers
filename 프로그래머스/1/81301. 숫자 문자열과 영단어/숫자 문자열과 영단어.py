def solution(s):
    new_s=''
    hashmap={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}

    for i in range(len(s)):
        if s[i].isdigit():
            new_s+=str(s[i])
        else:          
            if s[i:i+3] in hashmap:
                new_s+=(hashmap[s[i:i+3]])
            elif s[i:i+4] in hashmap:
                new_s+=(hashmap[s[i:i+4]])
            elif s[i:i+5] in hashmap:
                new_s+=(hashmap[s[i:i+5]])
    
    return int(new_s)
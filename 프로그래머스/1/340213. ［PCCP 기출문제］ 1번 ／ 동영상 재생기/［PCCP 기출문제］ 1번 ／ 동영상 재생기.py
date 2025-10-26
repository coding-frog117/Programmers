def solution(video_len, pos, op_start, op_end, commands):
    def getTime (time):
        minutes,seconds = time.split(":")
        return (int(minutes) * 60) + int(seconds)
    
    cur_pos = getTime(pos)
    op_start = getTime(op_start)
    op_end = getTime(op_end) 
    if op_start <= cur_pos <= op_end:
        cur_pos = op_end
    for c in commands :
        if c == "next" :
            cur_pos += 10
            if cur_pos > getTime(video_len):
                cur_pos = getTime(video_len)
        else :
            cur_pos -= 10 
            if cur_pos < 0 :
                cur_pos = 0
        if op_start <= cur_pos <= op_end:
            cur_pos = op_end
            
    minutes, seconds = divmod(cur_pos,60)
    minutes= str(minutes)
    seconds = str(seconds)
    
    if len(minutes) == 1:
        minutes = "0"+str(minutes)
    if len(seconds) == 1:
        seconds = "0" + str(seconds)
    return minutes + ":" + seconds
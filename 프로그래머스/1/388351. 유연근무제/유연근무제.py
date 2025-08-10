def solution(schedules, timelogs, startday):
    answer = 0
    
    saturday = 6 - startday
    sunday = 7- startday
    
    if saturday == -1:
        saturday = 6
    
    for log_idx,log in enumerate(timelogs):
        is_possible = True
        start_valid_hour, start_valid_minutes = divmod(schedules[log_idx],100)
        end_valid_hour = start_valid_hour
        end_valid_minutes = start_valid_minutes + 10
        if (end_valid_minutes >= 60) :
            end_valid_hour +=1 
            end_valid_minutes -= 60
            
        end_time = (end_valid_hour * 60) + end_valid_minutes
        for idx,time in enumerate(log):
            if idx == saturday or idx == sunday :
                continue
            
            hour,minutes = divmod(time,100)
            cur_time = (hour* 60) + minutes
            if cur_time > end_time:
                is_possible = False
                break
        if is_possible :
            answer += 1
        
    return answer
def solution(book_time):
    reservations = [0]*1440
    for time in book_time:
        [start,end] = time
        s_h,s_m = start.split(':')
        e_h,e_m = end.split(':')
        time_start = int(s_h)*60+int(s_m)
        time_end = int(e_h)*60+int(e_m)+10
        if time_end > 1439:
            time_end = 1439
        for i in range(time_start,time_end):
            reservations[i] += 1
            
    return max(reservations)
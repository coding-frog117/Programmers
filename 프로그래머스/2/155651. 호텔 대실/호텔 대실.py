def solution(book_time):
    room = 1
    empty = [[['00:00','23:59']]]
    book_time.sort()
    
    for time in book_time:
        [start,end] = time
        s_h,s_m = start.split(':')
        e_h,e_m = end.split(':')
        isPossible = False
        
        for roomidx,cur_room in enumerate(empty):
            roomFill = False
            for idx,emp_time in enumerate(cur_room):
                [emp_s,emp_e] = emp_time
                emp_s_h, emp_s_m = emp_s.split(':')
                emp_e_h, emp_e_m = emp_e.split(':')
                
                if not(int(emp_s_h) < int(s_h) or (int(emp_s_h) == int(s_h) and int(emp_s_m) <= int(s_m))):
                    continue
                if not(int(emp_e_h) > int(e_h) or (int(emp_e_h)==  int(e_h) and int(emp_e_m) >= int(e_m))):
                    continue
                isPossible = True
                roomFill = True
                addTime = []
                if emp_s != start:
                    time_h = int(s_h)
                    time_m = int(s_m)-10
                    if time_m < 0:
                        time_m = 60 + time_m
                        time_h -= 1
                    addTime.append([emp_s,f'{time_h}:{time_m}'])
                if emp_e != end:
                    time_h = int(e_h)
                    time_m = int(e_m)+10
                    if time_m >= 60:
                        time_m = time_m - 60
                        time_h += 1
                    addTime.append([f'{time_h}:{time_m}',emp_e])
                    
                empty[roomidx] = empty[roomidx][0:idx] + addTime + empty[roomidx][idx+1:]
            if roomFill:
                break
                
        if not isPossible :
            empty.append([])
            if emp_s != start:
                time_h = int(s_h)
                time_m = int(s_m)-10
                if time_m < 0:
                    time_m = 60 +time_m
                    time_h -= 1
                empty[-1].append(['00:00',f'{time_h}:{time_m}'])
            
            if emp_e != end:
                time_h = int(e_h)
                time_m = int(e_m)+10
                if time_m >= 60:
                    time_m = time_m - 60
                    time_h += 1
                empty[-1].append([f'{time_h}:{time_m}','23:59'])
    return len(empty)
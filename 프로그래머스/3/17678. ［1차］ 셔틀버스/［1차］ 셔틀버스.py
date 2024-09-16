# 마지막 셔틀 탈 수 있는 사람 수가 m*n 이상이면 마지막 사람보다 1분 빨리 오면 됨
# 그렇지 않다면 마지막 셔틀 시간에 도착

from collections import deque

def solution(n, t, m, timetable):
    timetable.sort()
    for idx,time in enumerate(timetable):
        hour,minuets = time.split(':')
        timetable[idx] = int(hour)*60+int(minuets)
        
    timetable = deque(timetable)

    bus = []
    cur_bus = 540
    cnt = 0
    bus_cnt = 1
    
    while bus_cnt <= n:
        if timetable[0] <= cur_bus:
            bus.append(timetable.popleft())
            cnt+= 1
        elif timetable[0] > cur_bus :
            if bus_cnt == n:
                break
            cnt = 0
            cur_bus += t
            bus_cnt += 1
            
        if cnt >= m:
            if bus_cnt == n:
                break
            cnt = 0
            cur_bus += t
            bus_cnt += 1
        if not timetable :
            break
    
    def changeTime(time):
        ans_h,ans_m = map(str,divmod(time,60))
        if len(ans_h) == 1:
            ans_h = '0' + ans_h
        if len(ans_m) == 1:
            ans_m = '0' + ans_m
        ans = ans_h + ':' + ans_m
        return ans
            
    if cnt < m:
        return changeTime(cur_bus)
    else:
        lastTime = bus[-1]-1
        return changeTime(lastTime)
# 시간표 길이 < m*n 이면 셔틀이 마지막에 오는 시간을 return
# 그렇지 않다면 현재 셔틀 시간을 탈 수 있는 사람 체크
# 마지막 셔틀 탈 수 있는 사람 수가 m*n 이상이면 탈 수 있는 시간 구함
# 만약 다 같다면 그것보다 빠른 시간, 만약 이전 셔틀에 탄 시간도 다 같다면 그것보다 빠른시간 - 셔틀에 탄 사람 시각을 모두 저장해둠
from collections import deque

def solution(n, t, m, timetable):
    timetable.sort()
    for idx,time in enumerate(timetable):
        hour,minuets = time.split(':')
        timetable[idx] = int(hour)*60+int(minuets)
        
    timetable = deque(timetable)

    bus = [[] for i in range(n)]
    cur_bus = 540
    cnt = 0
    bus_cnt = 1
    
    while bus_cnt <= n:
        if timetable[0] <= cur_bus:
            bus[bus_cnt-1].append(timetable.popleft())
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
            
    if len(bus[-1]) < m:
        return changeTime(cur_bus)
    else:
        lastTime = bus[-1][-1]-1
        return changeTime(lastTime)
                    
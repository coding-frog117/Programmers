import math

def solution(n, stations, w):
    ans = 0
    range_start = 0
    range_end = 0
    
    for idx,station in enumerate(stations):
        if idx == 0 :
            if station-w-1 > 0:
                range_start = 0
            else:
                range_end = station-w-1
                continue
        else:
            range_start = range_end+(w*2)+1
        range_end = station-w-1
        print(range_start,range_end)
        ans += math.ceil((range_end - range_start)/(w*2+1))
    
    if stations[-1]+w < n:
        ans += math.ceil((n-(stations[-1]+w))/(w*2+1))
    return ans
def getMinutes(time):
    hour, minutes = time.split(":")
    return int(hour) * 60 + int(minutes)

def solution(plans):
    plans = [[name, getMinutes(start), int(playtime)] for name, start, playtime in plans]
    plans.sort(key=lambda x: x[1])

    answer = []
    stack = []

    for i in range(len(plans) - 1):
        name, start, playtime = plans[i]
        next_start = plans[i + 1][1] 

        time_left = playtime - (next_start - start)

        if time_left > 0:
            stack.append([name, time_left])
        else:
            answer.append(name)
            free_time = -time_left 

            # 스택에 멈춘 과제가 있으면 이어서 수행
            while free_time > 0 and stack:
                prev_name, prev_left = stack.pop()
                if prev_left <= free_time:
                    free_time -= prev_left
                    answer.append(prev_name)
                else:
                    stack.append([prev_name, prev_left - free_time])
                    free_time = 0

    answer.append(plans[-1][0])

    while stack:
        answer.append(stack.pop()[0])

    return answer
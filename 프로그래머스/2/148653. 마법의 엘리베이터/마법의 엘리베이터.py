def solution(storey):
    cur_num = storey
    cnt = 0
    while cur_num != 0:
        length = len(str(abs(cur_num)))
        changed_num = int(str(abs(cur_num))[0])
        if int(str(abs(cur_num))[0]) > 5:
            if cur_num > 0:
                cur_num -= 10**length
            else:
                cur_num += 10**length
            cnt += 1
        elif int(str(abs(cur_num))[0]) == 5:
            if length > 1 and int(str(abs(cur_num))[1]) >= 5:
                if cur_num > 0:
                    cur_num -= 10**length
                else:
                    cur_num += 10**length
                cnt += 1
            else:
                if cur_num > 0:
                    cur_num -= changed_num*(10**(length-1))
                else:
                    cur_num += changed_num*(10**(length-1))
                cnt += changed_num
        else:
            if cur_num > 0:
                cur_num -= changed_num*(10**(length-1))
            else:
                cur_num += changed_num*(10**(length-1))
            cnt += changed_num
        print(cur_num,cnt)
    return cnt
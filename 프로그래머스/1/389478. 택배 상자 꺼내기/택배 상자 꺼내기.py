def solution(n, w, num):
    height = 0
    if w == 1:
        height = n // w
    else:
        height = (n // w) + 1
    arr = [[0 for i in range(w)] for _ in range(height)]
    count = 1
    inverse_count = w
    is_reverse = False
    floor = -1
    position = -1
    
    for y_idx,y in enumerate(arr):
        for x_idx,x in enumerate(y):
            if is_reverse:
                arr[y_idx][inverse_count-1] = count
                if count == num :
                    position = inverse_count-1
                inverse_count -= 1
            else :
                arr[y_idx][x_idx] = count
                if count == num :
                    position = x_idx
            if count == num :
                floor = y_idx
            if count % w == 0:
                is_reverse = not is_reverse
                inverse_count = w
            
            
            count += 1
            if count > n :
                break
    
    if arr[-1][position] == 0:
        return height - floor - 1
    return height - floor
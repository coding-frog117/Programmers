def solution(n):
    target = n
    ans = 0
    while target:
        if target % 2 == 0:
            target = target // 2
        else:
            target -= 1
            ans += 1
    return ans
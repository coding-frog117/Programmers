import math

# 제곱의 합이 d*2보다 크면 break
# d의 절반까지만 확인하면 됨. (홀수면 d/2 + 1까지)
# x를 하나씩 늘려가면서 최대 y값을 확인하여 가능한 점 갯수 파악
# 이전 y 값 저장해두고 차례대로 확인하기
def solution(k, d):
    count = 0
    prev_x = 0
    prev_y = (d//k) * k

    for x in range(0,d+1,k):
        prev_x = x
        for y in range(prev_y,-1,-k):
            if (x*x) + (y*y) <= d*d:
                prev_y = y
                x_possible_dot = (y-x)//k
                if x_possible_dot < 0:
                    break
                count += (x_possible_dot * 2 + 1)
                break
    return count
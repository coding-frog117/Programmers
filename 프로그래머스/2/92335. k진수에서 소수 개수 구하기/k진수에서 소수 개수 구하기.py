# 접근 - 진법변환 후 네가지 경우 체크
# 1. 맨 왼쪽 0전까지의 수
# 2. 맨 오른쪽 0이후의 수
# 3. 0과 0사이에 있는 수
# 4. 변환된 수 자체(0이 포함되지 않는다면)
# 이후 소수 판별은 어떻게??..

import math

def isPrime(num):
    for i in range(3,math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    candidates = []
    invert = ''

    if k == 10:
        invert = str(n)

    else:
        while n > 0:
            n, mod = divmod(n, k)
            invert = str(mod) + invert

    newInvert = invert.split('0')
    for i in newInvert:
        if i != '':
            candidates.append(int(i))
    # 소수 판별 함수
    # 에라토스테네스 체 algorithms
    # sqrtNum = math.ceil(math.sqrt(max(candidates)))+1
    # primeNums = [True for i in range(max(candidates) + 1)]
    # primeNums[0], primeNums[1] = False, False
    #
    # for i in range(2, sqrtNum):
    #     if primeNums[i] == True:
    #         j = 2
    #         while True:
    #             if i * j >= len(primeNums):
    #                 break
    #             primeNums[i * j] = False
    #             j += 1
    #
    ans = 0
    
    for i in candidates:
        if i == 1:
            continue
        if isPrime(i) == True:
            ans += 1

    return ans
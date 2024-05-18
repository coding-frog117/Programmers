from collections import deque

T = int(input())
for tc in range(T):
    n,m = map(int,input().split())
    fees = [0]
    weight = [0]

    for i in range(n):
        fee = int(input())
        fees.append(fee)

    for i in range(m):
        curr = int(input())
        weight.append(curr)
    answer = 0
    waitingQueue = deque()
    runningMap ={}
    for i in range(1,n+1):
        runningMap[i] = False

    for i in range(2*m):
        car =int(input())
        if car >0 :
            isParking = False
            for key, value in runningMap.items():
                if value == False:
                    runningMap[key] = [car]
                    answer += weight[car] * fees[key]
                    isParking = True
                    break
            if isParking == False :
                waitingQueue.append(car)
        else :
            for key, value in runningMap.items():
                if value == [-1 * car]:
                    runningMap[key] = False
                    if len(waitingQueue) > 0 :
                        putCar = waitingQueue.popleft()
                        runningMap[key] = [putCar]
                        answer += weight[putCar] * fees[key]

    print(f'#{tc+1} {answer}')
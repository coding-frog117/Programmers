from collections import deque
T = int(input())

def R(arr,isReversed,n):
    if n == 0:
        return []
    if isReversed:
        newArr = str(list(reversed(list(arr)))).replace(' ','')
        return newArr
    else:
        return str(list(arr)).replace(' ','')

def D(arr,isReverse):
    if len(arr) <= 0 or arr == deque(['']):
        return False
    if isReverse :
        arr.pop()
    else:
        arr.popleft()

for i in range(T):
    p = list(input())
    n = int(input())
    inp = input()[1:-1].split(',')
    if inp !=['']:
        queue = deque(list(map(int,inp)))
    else:
        queue = deque([''])
    isReversed = False
    isPossible= True

    for i in p:
        if i == 'R':
            isReversed = not isReversed
        else:
            result = D(queue,isReversed)
            if result == False:
                isPossible = False
                print('error')
                break
    if isPossible:
        print(R(queue,isReversed,n))
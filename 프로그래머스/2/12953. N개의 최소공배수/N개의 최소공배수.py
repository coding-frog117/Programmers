def find(a,b):
    minNum = a*b
    for i in range(1,a*b+1):
        if i % a == 0 and i % b == 0:
            minNum = i
            break
    return minNum
    
def solution(arr):
    if len(arr) == 1:
        return arr[0]
    ans = 0
    prev = arr[0]
    for i in range(1,len(arr)):
        prev = find(prev,arr[i])
    return prev
        
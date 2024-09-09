def solution(sequence):
    purse1 = []
    purse2= []
    purse1_mul = 1
    purse2_mul = -1
    for num in sequence:
        purse1.append(num*purse1_mul)
        purse2.append(num*purse2_mul)
        purse1_mul *= -1
        purse2_mul *= -1
    
    def findSum(arr):
        maxSum = 0
        prevSum = 0
        start = 0
        end = 0
        
        while start < len(arr) and end < len(arr):
            if prevSum+arr[end] < arr[end]:
                start = end
                prevSum = arr[end]
            else:
                prevSum += arr[end]
            maxSum = max(maxSum,prevSum)
            end += 1
        return maxSum
    
    ans = max(findSum(purse1),findSum(purse2))
    return ans
N,K = map(int,input().split())
numberArr = list(map(int,input().split()))

global startIdx
global endIdx
startIdx = 0
endIdx = K
global maxSum
maxSum = sum(numberArr[startIdx:endIdx])
global currentSum
currentSum = sum(numberArr[startIdx:endIdx])

while (endIdx < len(numberArr)):
  currentSum = currentSum + numberArr[endIdx] - numberArr[startIdx]
  if (currentSum> maxSum) :
    maxSum = currentSum
  startIdx += 1
  endIdx += 1

print(maxSum)
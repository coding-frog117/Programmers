N,S = map(int,input().split())
arr = list(map(int,input().split()))

start =0
end = 0
sum = arr[0]
global minLen
minLen = N+1

while (end < N):
  if (sum < S):
    end += 1
    if (end > N-1):
      break
    sum += arr[end]
    
  elif (sum >= S):
    minLen = min(minLen,end-start+1)
    sum -= arr[start]
    start += 1

answer = minLen if (minLen <= len(arr)) else 0
print(answer)
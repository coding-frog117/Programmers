N,M = map(int,input().split())
arr = list(map(int,input().split()))

start = 0
end = 0
sum = arr[start]
answer = 0

while end < len(arr):
  if sum < M:
    end+= 1
    if end >= N:
      break
    sum += arr[end]
  elif sum > M:
    sum -= arr[start]
    start += 1
    if start < 0 :
      break
  elif sum == M:
    answer += 1
    start += 1
    end = start

    if end >= N:
      break
    sum = arr[start]
print(answer)
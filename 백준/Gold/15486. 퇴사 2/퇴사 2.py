N= int(input())
days = []
income = []
maxVal = 0
arr = [0]*N

for i in range(N):
  d,i = map(int,input().split())
  days.append(d)
  income.append(i)

for i in range(N-1,-1,-1):
  if days[i] + i > N:
    arr[i] = maxVal
  elif days[i] + i == N:
    arr[i] = max(income[i],maxVal)
    maxVal = max(maxVal,arr[i])
  else:
    arr[i] = max(income[i] + arr[days[i]+i],maxVal)
    maxVal = max(maxVal,arr[i])
print(arr[0])